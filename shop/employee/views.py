from django.shortcuts import render
from .models import Employee_attendance
# Create your views here.


def employee_attendance(request):
     # Query attendance data and format it for the template
    attendance_records = Employee_attendance.objects.select_related('employee').all()
    
    # Prepare the data to match the template's structure
    attendances = [
        {
            'date': record.check_in,  # Use check_in date for the attendance date
            'employee_name': record.employee.name,
            'status': 'Present' if record.status else 'Absent'
        }
        for record in attendance_records
    ]

    # Pass the data to the template
    context = {
        'attendances': attendances,
    }
    return render(request, 'employee/employee_attendance.html', context)