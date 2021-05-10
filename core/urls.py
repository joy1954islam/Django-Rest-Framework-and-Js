from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('', views.personal_information_list, name='personal_information_list'),
    path('<int:pk>/', views.personal_information_detail, name='personal_information_detail'),
]
