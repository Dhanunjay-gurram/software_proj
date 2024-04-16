
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Spectators
from shows.models import Shows, Seats
from salesperson.models import Tickets_Info
from manager.models import Users
from django.db.models import Q
from django.contrib import auth 
from manager.models import BalanceSheet
from django.contrib import messages
from datetime import datetime, date


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('name')
        username = request.POST.get('userid')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        # Check if passwords match
        if password != confirm_password:
            return render(request, 'signup.html', {'error': 'Passwords do not match'})
        
        # Check if username is already taken
        if Spectators.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': 'Username already exists'})
        
        # Create Spectator object and save to database
        spectator = Spectators(first_name=first_name, username=username, password=password)
        spectator.save()
        
        return redirect('login') 
    
    return render(request, 'signup.html')

def sign_up(request):
    return render(request, 'signup.html')

@login_required
def spectator_profile(request):
    try:
        spectator = Spectators.objects.get(username=request.user)
    except Spectators.DoesNotExist:
        return redirect('login')  

    if request.method == 'POST':
        new_password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        new_name = request.POST.get('name')
        
        # Check if passwords match
        if new_password != confirm_password:
            return render(request, 'spectator_profile.html', {'spectator': spectator, 'error': 'Passwords do not match'})
        
        # Update password if changed
        if new_password:
            spectator.password = new_password

        # Update name if changed
        if new_name:
            spectator.first_name = new_name
        
        spectator.full_clean()
        spectator.save()

        return redirect('spectator_profile')

    context = {'spectator': spectator}
    return render(request, 'spectator_profile.html', context)

@login_required
def spectator_dashboard(request):
    username = request.user.first_name 
    shows = Shows.objects.all()  
    return render(request, 'spectator_dashboard.html', {'username': username, 'shows': shows})

@login_required
def book_ticket_spectator(request, show_id):
    if request.method == 'POST':
        sales_id = request.POST.get('salesperson')
        seat_no = request.POST.get('seat')
        name = request.POST.get('name')
        
        # Retrieve the selected show
        selected_show = Shows.objects.get(pk=show_id)
        
        # Check if the selected seat is available
        selected_seat = Seats.objects.filter(show_id=show_id, seat_no=seat_no, empty=True).first()
        if not selected_seat:
            messages.error(request, 'Selected seat is not available.')
            return redirect('book_ticket_spectator', show_id=show_id)
        
        # Calculate price to pay
        price = selected_show.balcony_rate if seat_no.startswith('B') else selected_show.ordinary_rate

        spectator = Spectators.objects.get(username=request.user)
        if spectator.wallet < price:
            messages.error(request, 'Wallet Amount is not sufficient.')
            return redirect('book_ticket_spectator', show_id=show_id)

        spectator.wallet -= price # Deduct price from Wallet
        spectator.save()

        salesperson = Users.objects.get(sales_id=sales_id)
        salesperson.wallet +=price
        salesperson.save()

        # Mark Seat as booked
        selected_seat.empty = False
        selected_seat.save()
        
        # Save booking details to TicketsInfo table
        Tickets_Info.objects.create(
            seat_no=seat_no,
            show_name=selected_show.show_name,
            date=selected_show.date,
            timing=selected_show.timing,
            seat_type='Balcony' if seat_no.startswith('B') else 'ordinary', 
            price=price,
            username=name,
            show_id=show_id,
            sales_id=sales_id  
        )
        
        # Add entry to BalanceSheet table
        BalanceSheet.objects.create(
            show_id=show_id,
            date=date.today(),  # Set the transaction date as the current date
            amount=price,
            type='Ticket Booking',
            sales_id=sales_id
        )
        
        messages.success(request, 'Ticket booked successfully.')
        return redirect('my_bookings_spectator')  # Redirect to spectator's bookings
        
    else:
        salespersons = Users.objects.filter(~Q(sales_id=0))
        seats = Seats.objects.filter(show_id=show_id, empty=True)
        
        return render(request, 'book_ticket_spectator.html', {'salespersons': salespersons, 'seats': seats})

@login_required
def my_bookings_spectator(request):
    spectator_name = request.user.first_name
    bookings = Tickets_Info.objects.filter(username=spectator_name)
    return render(request, 'my_bookings_spectator.html', {'username': spectator_name, 'bookings': bookings})

@login_required
def wallet(request):
    user_profile = Spectators.objects.get(username=request.user)
    wallet_balance = user_profile.wallet
    
    if request.method == 'POST':
        amount = request.POST.get('amount')
        if amount:
            user_profile.wallet += float(amount)
            user_profile.save()
            return redirect('wallet')
    
    return render(request, 'wallet.html', {'wallet_balance': wallet_balance})

@login_required
def cancel_booking_spectator(request, booking_id):
    if request.method == 'POST':
        booking = Tickets_Info.objects.get(booking_id=booking_id)
        seat = Seats.objects.get(show_id=booking.show_id, seat_no=booking.seat_no)

        date = datetime.strptime(booking.date, '%Y-%m-%d').date()
        
        # Calculate the difference between the show date and today
        show_date = datetime.combine(date, booking.timing)
        difference = show_date.date() - datetime.today().date()

        # Calculate the refund based on the cancellation timing
        if difference.days >= 3:
            refund = booking.price - 5  # Rs. 5 deduction for booking charge per ticket
        elif 1 <= difference.days < 3:
            if booking.seat_type == 'ordinary':
                refund = booking.price - 10  # Rs. 10 deduction for ordinary tickets
            else:
                refund = booking.price - 15  # Rs. 15 deduction for balcony tickets
        else:
            refund = booking.price / 2  # 50% deduction on the last day of the show

        # Refund the amount to the balance sheet
        BalanceSheet.objects.create(
            show_id=booking.show_id,
            date=datetime.today().date(),
            amount=(-refund),
            type='Refund',
            sales_id=booking.sales_id,
            txn_id=None 
        )

        user = Spectators.objects.get(username=request.user)
        user.wallet += refund # Add Refund back to account
        user.save()

        salesperson = Users.objects.get(sales_id=booking.sales_id)
        salesperson.wallet -=refund
        salesperson.save()

        # Mark seat as empty
        seat.empty = True
        seat.save()

        # Delete booking info
        booking.delete()

        messages.success(request, 'Booking cancelled successfully!')
        return redirect('my_bookings_spectator')
    else:
        return redirect('my_bookings_spectator')
 
@login_required
def view_ticket_spectator(request, booking_id):
    ticket = Tickets_Info.objects.get(booking_id=booking_id)
    return render(request, 'view_ticket_spectator.html', {'ticket': ticket})

@login_required
def logout(request):
    auth.logout(request)
    return redirect('login')