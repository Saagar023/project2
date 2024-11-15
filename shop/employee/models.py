from django.db import models
import uuid

# Create your models here.
class Employee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    salary = models.CharField(max_length=200)
    dob = models.DateField()
    gender = models.CharField(max_length=200)
    citizenship = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Employee_attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    check_in = models.DateTimeField(null=True, blank=True)
    check_out = models.DateTimeField(null=True, blank=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.employee.name


class Employee_salary(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.CharField(max_length=200)

    def __str__(self):
        return self.employee.name

class Employee_leave(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    reason = models.CharField(max_length=200)

    def __str__(self):
        return self.employee.name

class Employee_loan(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.CharField(max_length=200)

    def __str__(self):
        return self.employee.name

class Employee_loan_payment(models.Model):
    employee=models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.CharField(max_length=200)
    def __str__(self):
        return self.employee.name
    