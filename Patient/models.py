from datetime import datetime
from django.db import models
from enum import unique
from pyexpat import model
from tabnanny import verbose
from django.db import models
from numpy import choose
from zmq import NULL
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import profile




class Patient (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # models.ForeignKey("app.Model", verbose_name=_(""), on_delete=models.CASCADE)
    type1='type1'
    type2='type2'
    diatype_choices=[
        
        (type1,'type1'),
        (type2,'type2')
    ]
    height= models.IntegerField(blank=True,null=True)
    age= models.IntegerField(blank=True,null=True)
    weight=models.IntegerField(blank=True,null=True)
    diatype=models.CharField (choices=diatype_choices,blank=True,null=True ,max_length=20)
    def __str__ (self):
        return str(self.user)
#     # when a new user sign up ---> blank patient tablec reated
@receiver(post_save, sender=User)
def create_Patient_profile(sender, instance, created, **kwargs):
    if created:
        Patient.objects.create(user=instance)

    
class Test (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)    
    tes1='A1C Test'                             
    tes2='Fasting Blood Sugar Test'
    tes3='Glucose Tolerance Test'
    tes4='Random Blood Sugar Test'
    tes5='Tests for Gestational Diabetes'
    tes6='Glucose Screening Test'
    tes7='Glucose Tolerance Test'
    tes8='Prevent Type 2 Diabetes'
    tes9='Diabetes Treatment Plan'
    test_choices=[
        (tes1,'A1C Test'),                                
        (tes2,'Fasting Blood Sugar Test'),
        (tes3,'Glucose Tolerance Test'),
        (tes4,'Random Blood Sugar Test'),
        (tes5,'Tests for Gestational Diabetes'),
        (tes6,'Glucose Screening Test'),
        (tes7,'Glucose Tolerance Test'),
        (tes8,'Prevent Type 2 Diabetes'),
        (tes9,'Diabetes Treatment Plan')]
    tast_name=models.CharField(choices=test_choices,blank=True,null=True,max_length=200,default=NULL)
    time=models.DateTimeField(default=datetime.now)



class Medecin (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    medecin1='Actos '
    medecin2='Actrapid' 
    medecin3='Augmentin '
    medecin4='Amaryl '
    medecin5='Byetta '
    medecin6='Bydreoun' 
    medecin7='Competact' 
    medecin8='Diamicron '
    medecin9='Eucreas '
    medecin10='Forxiga '
    medecin11='Galvus '
    medecin12='Gliclazide'	 
    medecin13='Glucobay '
    medecin14='Humalog '
    medecin15='Humulin I' 
    medecin16='Hypurin Bovine Isophane' 
    medecin17='Hypurin Bovine Lente '
    medecin18='Hypurin Bovine Protamine Zinc'
    medecin19='Insulin Glulisine '
    medecin20='Insuman Basal '
    medecin21='Insuman Comb '
    medecin22='Janumet '
    medecin23='Januvia '
    medecin24='Lantus '
    medecin25='Lucentis' 
    medecin26='Lyxumia '
    medecin27='Metformin' 
    medecin28='NovoRapid '
    medecin29='Prandin '
    medecin30='Starlix '
    medecin31='Trulicity' 
    medecin32='Victoza '    
    medecin_choices=[
        (medecin1,'Actos '),
        (medecin2,'Actrapid'), 
        (medecin3,'Augmentin '),
        (medecin4,'Amaryl '),
        (medecin5,'Byetta '),
        (medecin6,'Bydreoun'), 
        (medecin7,'Competact'), 
        (medecin8,'Diamicron '),
        (medecin9,'Eucreas '),
        (medecin10,'Forxiga '),
        (medecin11,'Galvus '),
        (medecin12,'Gliclazide'),	 
        (medecin13,'Glucobay '),
        (medecin14,'Humalog '),
        (medecin15,'Humulin I'), 
        (medecin16,'Hypurin Bovine Isophane'), 
        (medecin17,'Hypurin Bovine Lente '),
        (medecin18,'Hypurin Bovine Protamine Zinc'), 
        (medecin19,'Insulin Glulisine '),
        (medecin20,'Insuman Basal '),
        (medecin21,'Insuman Comb '),
        (medecin22,'Janumet '),
        (medecin23,'Januvia '),
        (medecin24,'Lantus '),
        (medecin25,'Lucentis'), 
        (medecin26,'Lyxumia '),
        (medecin27,'Metformin'), 
        (medecin28,'NovoRapid '),
        (medecin29,'Prandin '),
        (medecin30,'Starlix '),
        (medecin31,'Trulicity'), 
        (medecin32,'Victoza ')
    ]
    medecin_name=models.CharField(choices=medecin_choices,blank=True,null=True,max_length=200,default=NULL)
    time=models.DateTimeField(default=datetime.now)
    def __str__ (self):
            return str(self.user)