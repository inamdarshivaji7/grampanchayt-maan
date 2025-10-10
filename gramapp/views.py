from django.shortcuts import get_object_or_404, render
from .models import Member,Employee

# Create your views here.
from django.http import HttpResponse

def index(request):
    top_members = Member.objects.all()[:3]
    return render(request, 'gramapp/index.html',{'top_members': top_members})

def member_list(request):
    members = Member.objects.all()[3:]

    return render(request, 'gramapp/members/member_list.html', {'members': members})

def employee_list(request):
    employees = Employee.objects.all()

    return render(request, 'gramapp/employee/employee_list.html', {'employees': employees})
def employee_profile(request, employee_id):
    
    employee = get_object_or_404(Employee, id=employee_id)
    return render(request, 'gramapp/employee/employee_profile.html', {'employee': employee})

def member_profile(request, member_id):
    
    member = get_object_or_404(Member, id=member_id)
    return render(request, 'gramapp/members/member_profile.html', {'member': member})