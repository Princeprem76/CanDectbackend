from django import forms
from django.core import validators
from .models import UserDetail, UserData


class CreateUserForm(forms.ModelForm):
    class Meta:
        model = UserDetail
        fields = '__all__'


class AdminLog(forms.Form):
    error_css_class = 'error'
    required_css_class = 'required'
    Useremail = forms.EmailField(label='Email', error_messages={'required':'Enter your email!'})
    Password = forms.CharField(widget=forms.PasswordInput, error_messages={'required':'Enter your password!'})


class CreateUserDetailForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = '__all__'
