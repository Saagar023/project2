from django.shortcuts import render

# Create your views here.
def sales_entry(request):
    return render(request, 'sales/sales_entry.html')