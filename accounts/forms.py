# accounts/forms.py
from django import forms
from django.contrib.auth.models import User
from .models import Department
from captcha.fields import CaptchaField

class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'id': 'id_password', 'placeholder': 'Enter password'})
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'id': 'id_confirm_password', 'placeholder': 'Confirm password'})
    )
    department = forms.ModelChoiceField(queryset=Department.objects.all())
    captcha = CaptchaField() 

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
