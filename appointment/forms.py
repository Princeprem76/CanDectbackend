from django import forms
from .models import AppointDetail


class AppointForm(forms.ModelForm):
    class Meta:
        model = AppointDetail
        fields = '__all__'

