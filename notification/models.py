from django.db import models
from userSignup.models import UserData, UserDetail


# Create your models here.
class notifyDetail(models.Model):
    Doctor_Name = models.ForeignKey(UserDetail, on_delete=models.CASCADE, max_length=120)
    Patient_Name = models.ForeignKey(UserData, on_delete=models.CASCADE, max_length=120)
    Date = models.DateField(auto_now=True)
    Mesage = models.TextField()
