
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.employee_attendance, name='employee_attendance'),
    path('add_employee/', views.add_employee, name='add_employee'),
    path('employee_list', views.list_employee, name='list_employee'),
    path('delete-employee/<uuid:employee_id>', views.delete_employee, name='delete_employee'),
    path('edit_employee/<uuid:employee_id>', views.edit_employee, name='edit_employee'),

]
