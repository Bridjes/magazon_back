from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CustomUserCreationForm(UserCreationForm):
    password = forms.CharField(widget=forms.HiddenInput())
    class Meta:
        model = User
        fields = '__all__'