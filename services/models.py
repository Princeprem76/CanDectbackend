from django.db import models


# Create your models here.
class AddService(models.Model):
    services = models.CharField(max_length=200)
    price = models.PositiveSmallIntegerField()
    def __str__(self):
        return self.services

