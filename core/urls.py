from django.contrib import admin
from django.urls import path
from core import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # API
    path('personal_information_list/', views.personal_information_list, name='personal_information_list'),
    path('personal_information_list/<int:pk>/', views.personal_information_detail, name='personal_information_detail'),

    path('', views.personal_information, name='personal_information')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
