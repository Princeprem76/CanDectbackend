from django.urls import path
from .views import DoctorData, AppointmentDoctor, Login_Doctor, updateDoctordetail, detection, ecgdetection, DoctorDatas

urlpatterns = [
    # path('doctorSignup/', Create_Doctorweb),
    path('doctorappointdetail/<int:serviceid>/', AppointmentDoctor),
    path('doctordetail/<str:doctoremail>/', DoctorData),
    path('doctordata/<str:doctoremail>/', DoctorDatas),
    path('doctorLogin/', Login_Doctor),
    path('updatedoctordetail/<str:doctoremail>/', updateDoctordetail),
    path('detect/', detection),
    path('ecgdetect/', ecgdetection),
]
