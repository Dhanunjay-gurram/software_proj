from django.shortcuts import render, redirect
from shows.models import Shows, Seats
from manager.models import Users
from salesperson.models import Tickets_Info
from manager.models import BalanceSheet
from django.contrib.auth.decorators import login_required
from django.contrib import auth 
from datetime import  datetime, date
from django.contrib import messages
from django.utils import timezone

@login_required
def salesperson_dashboard(request):
    return render(request, 'salesperson_dashboard.html')

@login_required
def cancel_ticket(request):
    return render(request, 'cancel_ticket.html')

@login_required
def logout(request):
    auth.logout(request)
    return redirect('login')

@login_required
def profile(request):
    try:
        salesperson = Users.objects.get(username=request.user)
    except Users.DoesNotExist:
        return redirect('login')  

    if request.method == 'POST':
        new_password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        new_name = request.POST.get('name')
        
        # Check if passwords match
        if new_password != confirm_password:
            return render(request, 'salesperson_profile.html', {'salesperson': salesperson, 'error': 'Passwords do not match'})
        
        # Update password if changed
        if new_password:
            salesperson.password = new_password

        # Update name if changed
        if new_name:
            salesperson.first_name = new_name
        
        salesperson.save()

        return redirect('profile')

    context = {'salesperson': salesperson}
    return render(request, 'salesperson_profile.html', context)

@login_required
def book_ticket(request):
    if request.method == 'POST':
        show_id = request.POST.get('show')
        seat_type = request.POST.get('seat_type')
        name = request.POST.get('name')
        
        # Retrieve the selected show
        selected_show = Shows.objects.get(pk=show_id)
        
        # Check if the selected show is in the past
        selected_date = datetime.strptime(selected_show.date, '%Y-%m-%d').date()
        if (selected_date) < (date.today()):
            shows = Shows.objects.all()  
            show_data = []

            for show in shows:
               balcony_seats_count = Seats.objects.filter(show_id=show.show_id, seat_no__startswith='B', empty=True).count()
               ordinary_seats_count = Seats.objects.filter(show_id=show.show_id, seat_no__startswith='O', empty=True).count()
               show_info = {
                  'show': show,
                  'balcony_seats_count': balcony_seats_count,
                  'ordinary_seats_count': ordinary_seats_count
               }
               show_data.append(show_info)
            return render(request, 'book_ticket.html', {'show_data': show_data, 'error': 'Selected show is in the past'})
        
        # Book the next available seat of the specified type
        if seat_type == 'balcony':
            available_seats = Seats.objects.filter(show_id=show_id, seat_no__startswith='B', empty=True)
        elif seat_type == 'ordinary':
            available_seats = Seats.objects.filter(show_id=show_id, seat_no__startswith='O', empty=True)
        
        if not available_seats.exists():
            return render(request, 'show_list.html', {'show_data': show_data, 'error': 'No available seats of the selected type'})
        
        # Get the first available seat and book it
        seat_to_book = available_seats.first()
        seat_to_book.empty = False
        seat_to_book.save()
        
        # Calculate the price based on seat type
        price = selected_show.balcony_rate if seat_type == 'balcony' else selected_show.ordinary_rate

        # Fetch the Users object corresponding to the logged-in user
        salesperson = Users.objects.get(username=request.user)
        sales_id = salesperson.sales_id

        salesperson.wallet += price # Add the price amount to wallet

        salesperson.save()
        
        # Save booking details to TicketsInfo table
        ticket = Tickets_Info.objects.create(
            seat_no=seat_to_book.seat_no,
            show_name=selected_show.show_name,
            date=selected_show.date,
            timing=selected_show.timing,
            seat_type=seat_type,
            price=price,
            username=name,
            show_id=show_id,
            sales_id=sales_id
        )
        
        # Add transaction entry to BalanceSheet table
        BalanceSheet.objects.create(
            show_id=show_id,
            date=date.today(),  # Set the transaction date as the current date
            amount=price,
            type='Ticket Booking',
            sales_id=sales_id
        )

        
        return redirect('my_bookings')
    
    else:
        today_date = timezone.now().date()
        shows = Shows.objects.filter(date__gte=today_date)
        show_data = []

        for show in shows:
            balcony_seats_count = Seats.objects.filter(show_id=show.show_id, seat_no__startswith='B', empty=True).count()
            ordinary_seats_count = Seats.objects.filter(show_id=show.show_id, seat_no__startswith='O', empty=True).count()
            show_info = {
                'show': show,
                'balcony_seats_count': balcony_seats_count,
                'ordinary_seats_count': ordinary_seats_count
            }
            show_data.append(show_info)    

        return render(request, 'book_ticket.html', {'show_data': show_data})

@login_required
def my_bookings(request):
    salesperson = Users.objects.get(username=request.user)
    sales_id = salesperson.sales_id
    bookings = Tickets_Info.objects.filter(sales_id=sales_id)
    return render(request, 'my_bookings_salesperson.html', {'bookings': bookings})

@login_required
def view_ticket(request, booking_id):
    ticket = Tickets_Info.objects.get(booking_id=booking_id)
    return render(request, 'ticket_details.html', {'ticket': ticket})

@login_required
def cancel_booking(request, username):
    booking = Tickets_Info.objects.get(username=username)
    seat = Seats.objects.get(show_id=booking.show_id, seat_no=booking.seat_no)

    date = datetime.strptime(booking.date, '%Y-%m-%d').date()
    
    show_date = datetime.combine(date, booking.timing)
    difference = show_date.date() - datetime.today().date()

    # Calculate the refund 
    if difference.days >= 3:
        refund = booking.price - 5 
    elif 1 <= difference.days < 3:
        if booking.seat_type == 'ordinary':
            refund = booking.price - 10  
        else:
            refund = booking.price - 15  
    elif 0<= difference.days < 1:
        refund = booking.price / 2  
    else:
        refund = 0    

    # Refund the amount to the balance sheet
    BalanceSheet.objects.create(
        show_id=booking.show_id,
        date=datetime.today().date(),
        amount=(-refund),
        type='Refund',
        sales_id=booking.sales_id,
        txn_id=None  
    )

    salesperson = Users.objects.get(username=request.user)
    salesperson.wallet -= refund 
    salesperson.save()

    seat.empty = True
    seat.save()

    booking.delete()

    messages.success(request, 'Booking cancelled successfully!')
    return redirect('my_bookings')

@login_required
def wallet_sp(request):
    user_profile = Users.objects.get(username=request.user)
    wallet_balance = user_profile.wallet
    
    if request.method == 'POST':
        if 'add_amount' in request.POST:
            amount = request.POST.get('add_amount')
            if amount:
                user_profile.wallet += float(amount)
                user_profile.save()
                return redirect('wallet_sp')
        elif 'withdraw_amount' in request.POST:
            amount = request.POST.get('withdraw_amount')
            if amount and float(amount) <= user_profile.wallet:
                user_profile.wallet -= float(amount)
                user_profile.save()
                return redirect('wallet_sp')
    
    return render(request, 'wallet_sp.html', {'wallet_balance': wallet_balance})