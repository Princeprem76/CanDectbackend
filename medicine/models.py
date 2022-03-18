from django.db import models

from doctorSignup.models import DoctorsData
from userSignup.models import UserData, UserDetail


# Create your models here.
class medicineDetail(models.Model):
    Doctor_Name = models.ForeignKey(DoctorsData, on_delete=models.CASCADE)
    Patient_Name = models.ForeignKey(UserData, on_delete=models.CASCADE)
    Disease = models.CharField(max_length=120)
    Date = models.DateField(auto_now=True)
    Medicine = models.TextField()

