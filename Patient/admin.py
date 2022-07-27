from django.contrib import admin
from .models import Patient,Medecin,Test
# Register your models here.

admin.site.register(Patient)
admin.site.register(Medecin)
admin.site.register(Test)