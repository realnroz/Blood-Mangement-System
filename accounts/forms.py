
from django import forms
from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm


from .models import User

class UserRegistrationForm(UserCreationForm):


    class Meta:
        model = User
        fields = ('email','password1','password2')


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']
