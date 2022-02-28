from django.db import models
from userSignup.models import UserData
from doctorSignup.models import DoctorsData
from services.models import AddService


# Create your models here.
class AppointDetail(models.Model):
    purpose = models.ForeignKey(AddService, on_delete=models.CASCADE)
    Doctor = models.ForeignKey(DoctorsData, on_delete=models.CASCADE)
    patient = models.ForeignKey(UserData, on_delete=models.CASCADE)
    date = models.DateField()
    times = models.TimeField()
    price = models.PositiveSmallIntegerField()
    # def __str__(self):
    #     return self.patient

