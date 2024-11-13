from django.shortcuts import render

# Create your views here.


def employee_attendance(request):
    return render(request,"employee/employee_attendance.html")