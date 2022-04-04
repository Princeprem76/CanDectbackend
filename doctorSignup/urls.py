from django.urls import path
from .views import DoctorData, AppointmentDoctor, Login_Doctor, updateDoctordetail, detection,ecgdetection

urlpatterns = [
    # path('doctorSignup/', Create_Doctorweb),
    path('doctorappointdetail/<int:serviceid>/', AppointmentDoctor),
    path('doctordetail/<str:doctoremail>/', DoctorData),
    path('doctorLogin/', Login_Doctor),
    path('updatedoctordetail/<str:doctoremail>/', updateDoctordetail),
    path('detect/', detection),
    path('ecgdetect/', ecgdetection),
]
