
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
import profile
from django.db.models.signals import post_save
from numpy import character

# Create your models here.

class Profile(models.Model):
    
    male ='male'
    female ='female'
    gender_choices=[
        (male,'male'),
        (female,'female')
    ]

    doctor ='doctor'
    patient ='patient'
    role_=[
        (doctor,'doctor'),
        (patient,'patient')
    ]

    role= models.CharField(choices=role_,blank=False,max_length=20,default='patient')
    user =models.OneToOneField(User ,on_delete=models.CASCADE)
    ssn=models.CharField (max_length=50, unique= False ,blank=True)
    phone=models.CharField (max_length=50,blank=True)
    city=models.CharField(max_length=70, blank=True)
    address= models.CharField(max_length=50,blank=True)
    gender=models.CharField (choices=gender_choices,blank=True , max_length=20)


    def __str__ (self):
        return str(self.user)

    # when a new user sign up ---> blank profile created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)