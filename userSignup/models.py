from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_doctoruser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class UserDetail(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(_('Email Address'), unique=True)
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    is_Verified = models.BooleanField(default=False)
    has_data = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin


class UserData(models.Model):
    selections = [('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')]
    FirstName = models.CharField('First Name', max_length=50)
    LastName = models.CharField('Last Name', max_length=50)
    age = models.PositiveSmallIntegerField('Age')
    phone = models.PositiveBigIntegerField('Phone Number', unique=True)
    gender = models.CharField('Gender', max_length=20, choices=selections, default='Female')
    address = models.CharField('Address', max_length=80)
    useremail = models.ForeignKey(UserDetail, on_delete=models.CASCADE)


    def __str__(self):
        return self.FirstName + " " + self.LastName
