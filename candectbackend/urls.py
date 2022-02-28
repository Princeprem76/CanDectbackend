"""candectbackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls import path, include

from appointment.views import Bookingdet
from doctorSignup.views import deleteDat, doctDat, doctorAdd, doctorEmailA, LogOut, editDoctor
from payment.views import viewPaymentData
from services.views import AdminService, editService, deleteserv
from userSignup.views import adminLogin



urlpatterns = [
    path('admin/', admin.site.urls),
    path('userapi/v1/', include('userSignup.urls')),
    path('doctorapi/v1/', include('doctorSignup.urls')),
    path('notifyapi/v1/', include('notification.urls')),
    path('medicineapi/v1/', include('medicine.urls')),
    path('appointapi/v1/', include('appointment.urls')),
    path('reportapi/v1/', include('report.urls')),
    path('service/v1/', include('services.urls')),
    path('paymentapi/v1/', include('payment.urls')),
    path('addDoctor/',doctorAdd, name='addDoctor'),
    path('signupdoctor/',doctorEmailA),
    path('adminLogin/', adminLogin),
    path('service/',AdminService),
    path('booking/',Bookingdet),
    path('payment/',viewPaymentData),
    path('home/', doctDat),
    path('delete/<str:id>/', deleteDat, name="Delete"),
    path('logout/', LogOut, name="Logout"),
    path('edit/<int:id>/', editDoctor, name="Edit"),
    path('editservice/<int:id>/', editService, name="Editservice"),
    path('deleteservice/<int:id>/', deleteserv, name="Deleteservice"),
]
