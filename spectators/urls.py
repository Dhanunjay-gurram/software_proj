# spectators/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.sign_up, name='sign_up'),
    path('register/', views.register, name='register'),
    path('profile/', views.spectator_profile, name='spectator_profile'),
    path('dashboard/', views.spectator_dashboard, name='spectator_dashboard'),
    path('my_bookings/', views.my_bookings_spectator, name='my_bookings_spectator'),
    path('book_ticket/<int:show_id>/',views.book_ticket_spectator, name='book_ticket_spectator'),
    path('wallet/', views.wallet, name='wallet'),
    path('cancel/<int:booking_id>/', views.cancel_booking_spectator, name='cancel_booking_spectator'),
    path('view/<int:booking_id>/', views.view_ticket_spectator, name='view_ticket_spectator'),
    path('logout/', views.logout, name='logout'),
]
