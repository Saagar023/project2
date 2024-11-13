
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.employee_attendance, name='employee_attendance'),
    
]
