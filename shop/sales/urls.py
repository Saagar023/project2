
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.sales_entry, name='sales_entry'),
    
]
