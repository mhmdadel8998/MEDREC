
from dataclasses import fields
from django import forms  
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm  
from django.core.exceptions import ValidationError  
from django.forms.fields import EmailField  
from django.forms.forms import Form  
from .models import Profile
class Signupform(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='')
    last_name = forms.CharField(max_length=30, required=True, help_text='')
    email = forms.EmailField(max_length=254,required=True, help_text='')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
   




class Userform(forms.ModelForm):
    class Meta:
        model = User
        fields=['first_name','last_name', 'email','username']


class Profileform (forms.ModelForm):
    class Meta:
        model=Profile
        fields=['ssn','phone','city','address','gender']