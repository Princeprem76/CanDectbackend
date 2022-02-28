from django.urls import path
from .views import CreateAppoint, AppointData, AppointdoctorData, Bookingdet

urlpatterns = [
    path('appoint/', CreateAppoint),
    path('viewAppoint/<int:userID>/', AppointData),
    path('viewdoctorAppoint/<int:userID>/', AppointdoctorData),
    
]
