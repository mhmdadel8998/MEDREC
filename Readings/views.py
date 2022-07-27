from sre_constants import IN
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from Patient.models import Patient,Test,Medecin
from Patient.forms import Patientform,Testform,Medecinform
from django.http import HttpResponse
from .forms import BP_form,Glucose_form, Insolineform
from .models import BloodP , Glucose, Insuline
from joblib import load
from django.db.models import Q
from django.shortcuts import  get_object_or_404
from accounts.models import Profile
from Readings.models import BloodP,Glucose,Insuline
model = load('SavedModels/model.joblib')
def myrecords(request):
    bloodp= BloodP.objects.filter(user__username=request.user)
    glucose= Glucose.objects.filter(user__username=request.user)
    insuline=Insuline.objects.filter(user__username=request.user)
    return render(request , 'readings/myrecords.html' ,{
        'bloodp': bloodp,
        'insuline':insuline,
        'gluecose':glucose})
def editrecord(request):
    if request.method=="POST": 
        p1=BloodP.objects.filter(user__username=request.user).last()
        p3=Glucose.objects.filter(user__username=request.user).last()
        p4=Insuline.objects.filter(user__username=request.user).last()
        blood=BP_form(request.POST,instance=p1)
        glucose=Glucose_form(request.POST,instance=p3)
        insuline=Insolineform(request.POST,instance=p4)
        if blood.is_valid() and glucose.is_valid() and insuline.is_valid:             
            change1=blood.save(commit=False)
            change1.user=request.user
            change1.save()
            change3=glucose.save(commit=False)
            change3.user=request.user
            change3.save()
            change4=insuline.save(commit=False)
            change4.user=request.user
            change4.save()
            BP_set=BloodP.objects.filter(user__username=request.user)
            glu_set=Glucose.objects.filter(user__username=request.user)
            ins_set=Insuline.objects.filter(user__username=request.user)
            return render(request , 'readings/myrecords.html' ,{
                    'bloodp': BP_set,
                    'gluecose':glu_set,
                    'insuline':ins_set})
    else:
        blood=BP_form()
        glucose=Glucose_form() 
        insuline=Insolineform()
    return render (request , 'readings/editrecord.html',{'blood': blood,'gluecose':glucose,'insuline':insuline})


def getPredictions(glucose, bloodpressure, insulin, bmi,age):

    prediction = model.predict([
        [glucose, bloodpressure,insulin, bmi,age]
    ])
    if prediction == 0:
        return 'Potentially not Diabetic'
    elif prediction == 1:
        return 'Potentially Diabetic'
    else:
        return 'Can Not Be Detirmined'

from .models import BloodP , Glucose, Insuline

def prediction(request):
    p1 = []
    p2 = []
    p3 = []
    p4 = []
    p5 = []
    p6 = []
    result="your result will apeare here"
    p=Profile.objects.get(user__username=request.user)
    if (p.role=="doctor"):
        if request.method=="POST":
            dsearch=request.session.get('dsearch')
            v1=BloodP.objects.filter(user__username=dsearch).last()
            p1.append(v1.value)
            v2=Glucose.objects.filter(user__username=dsearch).last()
            p2.append(v2.value)
            v3=Insuline.objects.filter(user__username=dsearch).last()
            p3.append(v3.value)
            v4=Patient.objects.get(user__username =dsearch)
            if not v1:
                result="Please inter blood pressure in the record"
            elif not v2:
                result="Please inter glucose level in the record"
            elif not v3:
                result="Please inter insuline level in the record"
            elif not v4:
                result="It seems that the profile mess some data"
            else:
                p4.append(v4.age)
                p5.append(v4.weight)
                p6.append(v4.height)
                weight=p5[-1]
                height=p6[-1]
                AGE=p4[-1]
                BMI=(weight)/((height/100)*(height/100))
                BP=p1[-1]
                GLU=p2[-1]
                INS=p3[-1]
                result = getPredictions( GLU, BP,INS,BMI,AGE)
    elif (p.role=="patient"):
        if request.method=="POST": 
            v1=BloodP.objects.filter(user__username=request.user).last()
            p1.append(v1.value)
            v2=Glucose.objects.filter(user__username=request.user).last()
            p2.append(v2.value)
            v3=Insuline.objects.filter(user__username=request.user).last()
            p3.append(v3.value)
            v4=Patient.objects.get(user__username =request.user)
            if not v1:
                result="Please inter blood pressure in the record"
            elif not v2:
                result="Please inter glucose level in the record"
            elif not v3:
                result="Please inter insuline level in the record"
            elif not v4:
                result="It seems that the profile mess some data"
            else:
                p4.append(v4.age)
                p5.append(v4.weight)
                p6.append(v4.height)
                weight=p5[-1]
                height=p6[-1]
                AGE=p4[-1]
                BMI=(weight)/((height/100)*(height/100))
                BP=p1[-1]
                GLU=p2[-1]
                INS=p3[-1]
                result = getPredictions( GLU, BP,INS,BMI,AGE)
    return render(request , 'readings/prediction.html' ,{'result':result})    

def chart(request):
    p=Profile.objects.get(user=request.user)
    if (p.role=="doctor"):
        dsearch=request.session.get('dsearch')
        profile=Profile.objects.get(user__username=dsearch)
        BP_set=BloodP.objects.filter(user__username=dsearch)
        glu_set=Glucose.objects.filter(user__username=dsearch)
        ins_set=Insuline.objects.filter(user__username=dsearch)
        BP_ordered=BP_set.order_by('time')[:500]
        glu_ordered=glu_set.order_by('time')[:500]
        ins_ordered=ins_set.order_by('time')[:500]
        patient=Patient.objects.get(user__username=dsearch)
    elif (p.role=="patient"):
        BP_set=BloodP.objects.filter(user__username=request.user).values("time", "value")
        glu_set=Glucose.objects.filter(user__username=request.user).values("time", "value")
        ins_set=Insuline.objects.filter(user__username=request.user).values("time", "value")
        BP_ordered=BP_set.order_by('time')[:500]
        glu_ordered=glu_set.order_by('time')[:500]
        ins_ordered=ins_set.order_by('time')[:500]
        profile=Profile.objects.get(user__username=request.user)
        patient=Patient.objects.get(user__username=request.user)
        
    return render(request , 'readings/chart.html' ,{'profile':profile,
                                                    'patient':patient,
                                                    'BP':BP_ordered,
                                                    'glucose':glu_ordered,
                                                    'ins':ins_ordered})

def check(request):
    return render(request , 'readings/check.html' ,{})