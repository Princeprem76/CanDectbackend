from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models

# Create your models here.
from services.models import AddService
from userSignup.models import UserManager, UserDetail
from django.utils.translation import gettext_lazy as _


class DoctorsData(models.Model):
    selections = [('Male', 'Male'), ('Female', 'Female')]
    prof = [('Physician', 'Physician'), ('Lab-Assistant', 'Lab-Assistant'), ('Oncologist', 'Oncologist'),
            ('Cardiologist', 'Cardiologist')]
    FirstName = models.CharField('First Name',max_length=50)
    LastName = models.CharField('Last Name', max_length=50)
    age = models.PositiveSmallIntegerField('Age')
    phone = models.PositiveBigIntegerField('Phone',unique=True)
    gender = models.CharField('Gender',max_length=30, choices=selections, default='--Select-one--')
    address = models.CharField('Address',max_length=80)
    speciality = models.CharField('Speciality',max_length=50, choices=prof, default='--Select-one--')
    field = models.ForeignKey(AddService, on_delete=models.CASCADE)
    Doctoremail = models.ForeignKey(UserDetail, on_delete=models.CASCADE)

    def __str__(self):
        return self.FirstName + " " + self.LastName
