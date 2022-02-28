from django.urls import path
from .views import Create_Medicine, MedicineData

urlpatterns = [
    path('medicine/', Create_Medicine),
    path('viewMedicine/<int:userID>/', MedicineData)

]
