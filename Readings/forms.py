from django import forms
from django.forms.forms import Form  
from .models import BloodP,Glucose,Insuline
from django.db import models
from datetime import datetime
from django.contrib.postgres.forms import SimpleArrayField


# class Bmi_form (forms.ModelForm):
#     class Meta:
#         model=Bmi
#         fields=['value','time']

class BP_form (forms.ModelForm):
    class Meta:
        model=BloodP
        fields=['value','time']

class Glucose_form (forms.ModelForm):
    class Meta:
        model=Glucose
        fields=['value','time']
        

class Insolineform (forms.ModelForm):
    class Meta:
        model=Insuline
        fields=['value','time']
