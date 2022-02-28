from django import forms
from .models import notifyDetail


class NotifyForm(forms.ModelForm):
    class Meta:
        model = notifyDetail
        fields = '__all__'
