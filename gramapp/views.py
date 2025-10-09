from django.shortcuts import render
from .models import Member,Employee

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, 'gramapp/index.html')

def member_list(request):
    members = Member.objects.all()[3:]

    return render(request, 'gramapp/members/member_list.html', {'members': members})

def employee_list(request):
    employees = Employee.objects.all()

    return render(request, 'gramapp/employee/employee_list.html', {'employees': employees})