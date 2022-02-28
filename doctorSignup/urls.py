from django.urls import path
from .views import DoctorData, AppointmentDoctor,Login_Doctor, updateDoctordetail

urlpatterns = [
    # path('doctorSignup/', Create_Doctorweb),
    path('doctorappointdetail/<int:serviceid>/', AppointmentDoctor),
    path('doctordetail/<int:doctoremail>/', DoctorData),
    path('doctorLogin/',Login_Doctor),
    path('updatedoctordetail/<int:doctoremail>/', updateDoctordetail),
]
