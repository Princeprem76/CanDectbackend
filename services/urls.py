from django.urls import path
from .views import CreateService, ServiceData, ServiceDataname,AdminService

urlpatterns = [
    path('service/', CreateService),
    path('viewservice/', ServiceData),
    path('viewservicename/<int:serviceid>/', ServiceDataname),
    
]
