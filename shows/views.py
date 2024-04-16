from django.shortcuts import render, redirect
from .models import Shows, Seats
from datetime import datetime
from django.db.models import Sum
from manager.models import BalanceSheet
from django.contrib import messages
from django.utils import timezone

def add_show(request):
    if request.method == 'POST':
        # Get common show details
        show_name = request.POST['show_name']
        date = request.POST['date']
        num_shows = int(request.POST['num_shows'])

        # Validate date to ensure it's not in the past
        if datetime.strptime(date, '%Y-%m-%d').date() < datetime.now().date():
            messages.error(request, 'Cannot add shows for past dates.')
            return redirect('add_show')

        # Iterate through each show and create/save them individually
        for i in range(num_shows):
            
            timing = request.POST[f'timing_{i}']
            end_time = request.POST[f'end_time_{i}']
            no_of_balcony_seats = int(request.POST[f'no_of_balcony_seats_{i}'])
            no_of_ordinary_seats = int(request.POST[f'no_of_ordinary_seats_{i}'])
            balcony_rate = int(request.POST[f'balcony_rate_{i}'])
            ordinary_rate = int(request.POST[f'ordinary_rate_{i}'])

            # Validate end time to ensure it's after start time
            if datetime.strptime(end_time, '%H:%M') <= datetime.strptime(timing, '%H:%M'):
                messages.error(request, 'End time must be after start time.')
                return redirect('add_show')
            
            # Save the show data to the database
            show = Shows.objects.create(
                show_name=show_name,
                date=datetime.strptime(date, '%Y-%m-%d'), 
                timing=timing,
                end_time=end_time,
                no_of_balcony_seats=no_of_balcony_seats,
                no_of_ordinary_seats=no_of_ordinary_seats,
                balcony_rate=balcony_rate,
                ordinary_rate=ordinary_rate,
            )

            # Add balcony seats for the show
            for j in range(no_of_balcony_seats):
                Seats.objects.create(seat_no=f'B-{j+1}', empty=True, show_id=show.show_id)

            # Add ordinary seats for the show
            for j in range(no_of_ordinary_seats):
                Seats.objects.create(seat_no=f'O-{j+1}', empty=True, show_id=show.show_id)
        messages.success(request, 'Show succesfully added.')
        return redirect('show_list')
    else:
        print(timezone.now().strftime('%H:%M'))
        return render(request, 'add_show.html')

def show_list(request):
    manager_id = request.user.username
    shows = Shows.objects.all()  
    show_data = []

    for show in shows:
        empty_balcony_seats_count = Seats.objects.filter(show_id=show.show_id, seat_no__startswith='B', empty=True).count()
        empty_ordinary_seats_count = Seats.objects.filter(show_id=show.show_id, seat_no__startswith='O', empty=True).count()
        
        total_amount_collected = BalanceSheet.objects.filter(show_id=show.show_id, sales_id__gt=0).aggregate(total_amount=Sum('amount'))['total_amount']
        
        show_info = {
            'show': show,
            'balcony_seats_count': round((empty_balcony_seats_count / show.no_of_balcony_seats) * 100, 2),
            'ordinary_seats_count': round((empty_ordinary_seats_count / show.no_of_ordinary_seats) * 100, 2),
            'total_amount_collected': total_amount_collected if total_amount_collected else 0,
        }
        show_data.append(show_info)

    return render(request, 'show_list.html', {'show_data': show_data, 'manager_id': manager_id})

