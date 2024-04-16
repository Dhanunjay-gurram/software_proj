
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.accountclerk_dashboard, name='accountclerk_dashboard'),
    path('profile/', views.accounts_profile, name='accounts_profile'),
    path('add_expense/',views.add_expenses, name='add_expenses'),
    path('view_expenses/', views.view_expenses, name='view_expenses'),
    path('edit_expense/<int:txn_id>/', views.edit_expense, name='edit_expense'),
    path('delete_expense/<int:txn_id>/', views.delete_expense, name='delete_expense'),
]
