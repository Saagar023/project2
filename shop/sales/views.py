from django.shortcuts import render

# Create your views here.
def sales_entry(request):
    return render(request, 'sales/sales_entry.html')
def daily_expense(request):
    return render(request, 'sales/daily_expense.html')
def calendar(request):
    return render(request, 'sales/Calendar.html')
def einfo(request):
    return render(request, 'sales/einfo.html')
def ins_entry(request):
    return render(request, 'sales/ins_entry.html')
def dsr(request):
    return render(request, 'sales/dsr.html')

