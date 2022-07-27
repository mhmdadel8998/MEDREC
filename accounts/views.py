from audioop import reverse
from urllib.request import Request
from django.http import HttpResponse, HttpResponseNotFound
from telnetlib import BM
from unicodedata import decimal
from unittest import result
from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import Signupform, Userform ,Profileform
from django import forms
from .models import Profile
import pandas
from django.views.generic import ListView
from Readings.utils import get_chart
from Readings.models import BloodP,Glucose ,Insuline
from Patient.models import Patient
from Patient.forms import Patientform
from Readings.urls import urlpatterns
# Create your views here.
from django.shortcuts import render
from Patient.models import Patient

def signup(request):
    if request.method == 'POST':
        form = Signupform(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = Signupform()
    return render(request, 'registration/signup.html', {'form': form})

def profile(request):
    BP_set=BloodP.objects.filter(user__username=request.user)
    glu_set=Glucose.objects.filter(user__username=request.user)
    ins_set=Insuline.objects.filter(user__username=request.user)
    BP_ordered=BP_set.order_by('time')[:500]
    glu_ordered=glu_set.order_by('time')[:500]
    ins_ordered=ins_set.order_by('time')[:500]
    profile=Profile.objects.get(user__username=request.user)
    patient=Patient.objects.get(user__username=request.user)
    return render(request , 'accounts/profile.html',{
        'profile':profile,
        'patient':patient,  
        'BP':BP_ordered,
        'glucose':glu_ordered,
        'ins':ins_ordered })


def edit_profile(request):
    profile=Profile.objects.get(user__username=request.user)
    patient=Patient.objects.get(user__username=request.user)
    if request.method=="POST":
        userform=Userform(request.POST,instance=request.user)
        profileform=Profileform(request.POST, instance=profile)
        patientform=Patientform(request.POST, instance=patient)
        if userform.is_valid and profileform.is_valid and patientform.is_valid:
            userform.save()
            change=profileform.save(commit=False)
            change.user=request.user
            change.save()
            change1=patientform.save(commit=False)
            change1.user=request.user
            change1.save()
            return render(request , 'accounts/profile.html',{'profile':profile,'patient':patient})

    else:
        userform=Userform(instance=request.user)
        profileform=Profileform(instance=profile) 
        patientform=Patientform(instance=patient)   


    return render (request , 'accounts/edit_profile.html',{'userform':userform,
                                                           'profileform':profileform, 
                                                           'patientform':patientform,
                                                           'profile':profile})

def patient_profile(request):
        if request.method == "GET":
            dsearch=request.GET['dsearch'] 
            request.session['dsearch']=dsearch 
            profile=Profile.objects.get(user__username =dsearch)
            if (profile.role=="doctor"):
                err="this is not a patient username please inetr another one"
                return render(request , 'accounts/profile.html',{'err':err})
            elif(profile.role=="patient"):
                BP_set=BloodP.objects.filter(user__username=dsearch)
                glu_set=Glucose.objects.filter(user__username=dsearch)
                ins_set=Insuline.objects.filter(user__username=dsearch)
                BP_ordered=BP_set.order_by('time')[:500]
                glu_ordered=glu_set.order_by('time')[:500]
                ins_ordered=ins_set.order_by('time')[:500]
                patient=Patient.objects.get(user__username=dsearch)
                return render (request,'accounts/patient_profile.html',{'profile':profile,'patient':patient,'BP':BP_ordered,
                                                          'glucose':glu_ordered,'ins':ins_ordered})
        else:
            err="not valid"
            return render(request , 'accounts/profile.html',{'err':err})
