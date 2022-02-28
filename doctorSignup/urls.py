from django.urls import path
from .views import DoctorData, AppointmentDoctor, Login_Doctor, updateDoctordetail, detection,ecgdetection

urlpatterns = [
    # path('doctorSignup/', Create_Doctorweb),
    path('doctorappointdetail/<int:serviceid>/', AppointmentDoctor),
    path('doctordetail/<int:doctoremail>/', DoctorData),
    path('doctorLogin/', Login_Doctor),
    path('updatedoctordetail/<int:doctoremail>/', updateDoctordetail),
    path('detect/', detection),
    path('ecgdetect/', ecgdetection),
]
