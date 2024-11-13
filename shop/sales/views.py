from django.shortcuts import render

# Create your views here.
def sales_entry(request):
    return render(request, 'sales/sales_entry.html')
def daily_expense(request):
    return render(request, 'sales/daily_expense.html')