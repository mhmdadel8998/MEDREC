from django.db import models
from datetime import datetime
from enum import unique
from pyexpat import model
from tabnanny import verbose
from numpy import choose
# from pages.models import Plogin
from zmq import NULL
# from django.contrib.postgres.fields import ArrayField
from Patient.models import Patient
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# saving uploaded image to archive.
# image nameing not correct
def image_upload(instance,filename):
    imagename,extention = filename.split(".")
    return "readings/%s/%s.%s"%( instance.id ,instance.id , extention)



# Create your models here.   
class BloodP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value= models.DecimalField( max_digits=5, decimal_places=2, default=0)
    time=models.DateTimeField(default=datetime.now)
    def __str__ (self):
        return str(self.user)

class Insuline(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value= models.DecimalField( max_digits=5, decimal_places=2, default=0)
    time=models.DateTimeField(default=datetime.now)
    def __str__ (self):
        return str(self.user)

class Glucose(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value=models.DecimalField( max_digits=5, decimal_places=2, default=0)
    time=models.DateTimeField(default=datetime.now)
    def __str__ (self):
        return str(self.user)