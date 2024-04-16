from django.contrib import admin
from django.urls import path
from shows.views import add_show, show_list
from django.contrib.auth import views as auth_views
from . import views
from shows.views import show_list


urlpatterns = [
    path('dashboard/',show_list, name='show_list'), 
    path('manager_profile/', views.manager_profile, name='manager_profile'),
    path('add_show/', add_show, name='add_show'),
    path('show_list/', show_list, name='show_list'),
    path('add_salesperson/', views.add_salesperson, name='add_salesperson'),
    path('view_balance_sheet/', views.view_balance_sheet, name='view_balance_sheet'),
    path('yearly_balance_sheet/', views.yearly_balance_sheet, name='yearly_balance_sheet'),
    path('salesperson_list/', views.salesperson_list, name='salesperson_list'),
    path('logout/', views.logout, name='logout'),
]
