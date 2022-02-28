from django.db import models

# Create your models here.
from services.models import AddService
from userSignup.models import UserData


class payments(models.Model):
    # select = [('E-payment', 'E-payment'), ('Cash', 'Cash')]
    price = models.PositiveIntegerField()
    payment_method = models.CharField(max_length=120)
    user = models.ForeignKey(UserData, on_delete=models.CASCADE)
    service = models.ForeignKey(AddService, on_delete=models.CASCADE)
    Date = models.DateTimeField(auto_now=True)
    payment_done = models.BooleanField()
