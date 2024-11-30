from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Employee_attendance, Employee
from .forms import EmployeeForm

User = get_user_model()

@login_required
def employee_attendance(request):
    attendance_records = Employee_attendance.objects.select_related('employee').all()
    attendances = [
        {
            'date': record.check_in,
            'employee_name': record.employee.name if record.employee else 'Unknown',
            'status': 'Present' if record.status else 'Absent',
        }
        for record in attendance_records
    ]
    return render(request, 'employee/employee_attendance.html', {'attendances': attendances})

# @login_required
# @user_passes_test(lambda u: u.is_staff)
def add_employee(request):
    if request.method == 'POST':
        print('post')
        form = EmployeeForm(request.POST)
        if form.is_valid():
            print('valid')
            employee = form.save(commit=False)
            is_admin = form.cleaned_data.get('admin')
            username = employee.name.lower().replace(" ", "")
            password = f'{username}123'
            email = employee.email
            print(username + password)

            if not User.objects.filter(username=username).exists():
                print('create user')
                user = User.objects.create_user(username=username, password=password, email=email)
                if is_admin:
                    user.is_staff = True
                    user.is_superuser = True
                user.save()
                print('save user')

                employee.user = user
                employee.save()
                messages.success(request,'User Successfully created')
                return redirect('list_employee')
            else:
                messages.error(request, 'User with the same username already exists')
                return redirect('add_employee')
    else:
        form = EmployeeForm()
    return render(request, 'employee/add_employee.html', {'form': form})

@login_required
def edit_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()

            messages.success(request, f'Employee {employee.name} has been updated successfully')

            return redirect('list_employee')
    else:
        form = EmployeeForm(instance=employee)

    return render(request, 'employee/update_employee.html', { 'employee': employee, 'form': form    })

@login_required
@user_passes_test(lambda u: u.is_staff)
def delete_employee(request, employee_id):
    try:
        employee = get_object_or_404(Employee, id=employee_id)

        # Delete the associated user first if necessary
        if employee.user:
            employee.user.delete()

        # Set the user field to None before deleting the employee
        employee.user = None
        employee.save()  # Save the employee record with the cleared user field

        # Delete the employee record from the database
        employee.delete()

        messages.success(request, "Employee and their associated user deleted successfully.")
        return redirect('list_employee')

    except Exception as e:
        messages.error(request, f"Error deleting employee: {str(e)}")
        return redirect('list_employee')



@login_required
def list_employee(request):
    employees = Employee.objects.all()
    return render(request, 'employee/list_employee.html', {'employees': employees})
