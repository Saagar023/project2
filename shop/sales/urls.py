
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.sales_entry, name='sales_entry'),
    path("daily_expense/", views.daily_expense, name='daily_expense'),
    path("calendar/", views.calendar, name='calendar'),
    path("einfo/", views.einfo, name='einfo'),
    path("ins_entry/", views.ins_entry, name='ins_entry'),
    path("dsr/", views.dsr, name='dsr'),
]
