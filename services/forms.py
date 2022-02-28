from django import forms
from django.core import validators
from django.forms import fields

from services.models import AddService

class createService(forms.ModelForm):
    class Meta:
        model = AddService
        fields = '__all__'
