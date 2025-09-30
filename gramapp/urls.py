from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),  # root of this app
    path('members/', views.member_list, name='member_list'),
]
