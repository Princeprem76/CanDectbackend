from django import forms
from .models import DoctorsData


class CreateDoctorForm(forms.ModelForm):
    class Meta:
        model = DoctorsData
        fields = '__all__'


class DoctorEmailForm(forms.Form):
    error_css_class = 'error'
    required_css_class = 'required'
    Useremail = forms.EmailField(label='Email', error_messages={'required':'Enter your email!'})
    Password = forms.CharField(widget=forms.PasswordInput, error_messages={'required':'Enter your password!'})
