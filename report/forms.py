from django import forms
from .models import ReportDetail


class ReportForm(forms.ModelForm):
    class Meta:
        model = ReportDetail
        fields = '__all__'
