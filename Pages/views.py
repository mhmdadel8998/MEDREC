from fnmatch import fnmatch
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
# from matplotlib.font_manager import _Weight
# from .models import Plogin
from Patient.models import Patient
from accounts.models import Profile
# from  Patient.forms import Patient_infoForm
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
def home(request):
    return render (request,'registration/phome.html',{})

def login(request):
    return render (request,'registration/login.html',{})

# def phome(request):
    
#     return render (request,'registration/phome.html',{})


# def plogin(request):
#     if request.method == 'POST':
#         username=request.POST['pusername']
#         password=request.POST['ppassword']
#         user=authenticate(request, username=username , password=password)
            
#         if user is not None:
#             login (request,user)
#             return redirect ('pprofile')
#         else:
#             messages.success(request , ("username or password is not correct, please try again or signup..."))
#             return redirect ('plogin')
        
#     else:
#         return render (request,'authenticate/plogin.html',{})    




# def plogout(request):
#     logout (request)
#     messages.success(request,("you logged out"))
#     return redirect ('home')     



# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data ['username']
#             password = form.cleaned_data['password1']
#             user=authenticate(username = username , password = password)
#             login (request,user)
#             return redirect ('pprofile')
        
#     else:
#         form = UserCreationForm()
        
#     return render (request,'pages/signup.html' ,{'form':form, })     
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # submitted = False
    # if request.method == 'POST':
    #     form =Patient_infoForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request, 'Account created successfully')
        
    # else :
    #     form =Patient_infoForm
    #     if 'submitted' in request.GET:
    #         submitted=True

    # form =Patient_infoForm
    # return render (request,'pages/signup.html' ,{'form':form , 'submitted':submitted})     
        

    # p_fname= request.POST.get('first_name')
    # p_lname = request.POST.get('last_name')
    # p_email= request.POST.get('email')
    # p_phone= request.POST.get('phone')
    # p_city= request.POST.get('city')
    # p_address= request.POST.get('address')
    # p_height= request.POST.get('height')
    # p_weight= request.POST.get('weight')
    # p_age= request.POST.get('Age')
    # p_diatype= request.POST.get('Diabetestype')
    # p_gender= request.POST.get('gender')
    
    # b= Patient_info(p_fname=p_fname,p_lname=p_lname ,p_email= p_email,p_phone=p_phone,p_city=p_city,p_address=p_address,p_height=p_height, p_weight=p_weight,p_age= p_age,p_diatype=p_diatype,p_gender=p_gender)
    # # data= plogin(p_fname,p_lname ,p_email,p_phone,p_city,p_address,p_height, p_weight,p_dateofbirth,p_diatype,p_gender)
    # b.save()
    
    # p_ssn = request.POST.get('ssn')
    # p_password = request.POST.get('password')
    
    # a= Plogin (p_ssn=p_ssn,p_password=p_password)
    # a.save()

# Create your views here.
