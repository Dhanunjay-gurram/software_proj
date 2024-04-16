
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.salesperson_dashboard, name='salesperson_dashboard'),
    path('profile/', views.profile, name='profile'),
    path('book_ticket/', views.book_ticket, name='book_ticket'),
    path('cancel_ticket/', views.cancel_ticket, name='cancel_ticket'),
    path('logout/', views.logout, name='logout'),
    path('my_bookings/', views.my_bookings, name='my_bookings'),
    path('wallet/', views.wallet_sp, name='wallet_sp'),
    path('cancel_booking/<str:username>/', views.cancel_booking, name='cancel_booking'),
    path('salesperson/view_ticket/<int:booking_id>/', views.view_ticket, name='view_ticket'),
]
