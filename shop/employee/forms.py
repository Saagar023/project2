from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'phone', 'address', 'email', 'salary', 'dob', 'gender', 'citizenship', 'admin']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'block w-full sm:w-1/2 px-3 py-2 border border-gray-300 rounded-lg shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm text-gray-900'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'block w-full sm:w-1/2 px-3 py-2 border border-gray-300 rounded-lg shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm text-gray-900'
            }),
            'address': forms.Textarea(attrs={
                'class': 'block w-full sm:w-1/2 px-3 py-2 border border-gray-300 rounded-lg shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm text-gray-900',
                'rows': 3
            }),
            'email': forms.EmailInput(attrs={
                'class': 'block w-full sm:w-1/2 px-3 py-2 border border-gray-300 rounded-lg shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm text-gray-900'
            }),
            'salary': forms.NumberInput(attrs={
                'class': 'block w-full sm:w-1/2 px-3 py-2 border border-gray-300 rounded-lg shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm text-gray-900',
                'min': '0'
            }),
            'dob': forms.DateInput(attrs={
                'class': 'block w-full sm:w-1/2 px-3 py-2 border border-gray-300 rounded-lg shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm text-gray-900',
                'type': 'date'
            }),
            'gender': forms.Select(attrs={
                'class': 'block w-full sm:w-1/2 px-3 py-2 border border-gray-300 rounded-lg shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm text-gray-900'
            }, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')]),
            'citizenship': forms.TextInput(attrs={
                'class': 'block w-full sm:w-1/2 px-3 py-2 border border-gray-300 rounded-lg shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm text-gray-900'
            }),
        }
