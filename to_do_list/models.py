from django.db import models
from django.utils.timezone import now
from datetime import time

from django.contrib.auth.models import User

class DateBajarildiModel(models.Model):
    date = models.DateField()

class BajarildiModel(models.Model):
    sarlavha = models.CharField(verbose_name="vazifa", max_length=200)
    tuliq_malumot = models.TextField()
    tugatilgan_muddat = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.sarlavha

    
class VazifaModel(models.Model):
    foydalanuvchi = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    sarlavha = models.CharField(verbose_name="vazifa", max_length=200)
    tuliq_malumot = models.TextField()
    tugatish_muddati = models.DateTimeField(null=True, blank=True)
    bajarilgan_vaqt = models.DateTimeField(null=True, blank=True)
    bajarildi = models.BooleanField(default=False)
    
    def __str__(self):
        return self.sarlavha
    

class UquvchiModel(models.Model):
    first_name = models.CharField(verbose_name="Ism", max_length=35)
    last_name = models.CharField(verbose_name="Familiya", max_length=23)

    
