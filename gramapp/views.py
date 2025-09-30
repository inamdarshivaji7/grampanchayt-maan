from django.shortcuts import render
from .models import Member

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, 'gramapp/index.html')

def member_list(request):
    members = Member.objects.all()[3:]

    return render(request, 'gramapp/members/member_list.html', {'members': members})
