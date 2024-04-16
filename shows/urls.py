# urls.py

from django.urls import path
from .views import add_show,show_list

urlpatterns = [
    path('add_show/', add_show, name='add_show'),
    path('show_list/', show_list, name='show_list'),
]
