from django import forms
from .models import medicineDetail


class MedicineForm(forms.ModelForm):
    class Meta:
        model = medicineDetail
        fields = '__all__'
