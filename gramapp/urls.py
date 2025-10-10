from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),  # root of this app
    path('members/', views.member_list, name='member_list'),
    path('employees/', views.employee_list, name='employee_list'),
    path('employee/<int:employee_id>/', views.employee_profile, name='employee_profile'),
    path('members/<int:member_id>/', views.member_profile, name='member_profile'),

]
