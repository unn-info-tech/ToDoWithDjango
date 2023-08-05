from django.db import models
from django.utils.timezone import now
from datetime import time

from django.contrib.auth.models import User

class DateBajarildiModel(models.Model):
    foydalanuvchi = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField()

    def __str__(self):
        return self.date.strftime("%Y-%m-%d")
    
    class Meta:
        ordering = ['date']
    
class VazifaModel(models.Model):
    foydalanuvchi = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    sarlavha = models.CharField(verbose_name="vazifa", max_length=200)
    tuliq_malumot = models.TextField()
    boshlanish_vaqti = models.TimeField(null=True, blank=True)
    tugatish_muddati = models.TimeField(null=True, blank=True)
    bajarilgan_date = models.ForeignKey(DateBajarildiModel, on_delete=models.CASCADE, null=True, blank=True)
    bajarilgan_vaqt =  models.TimeField(null=True, blank=True)
    bajarildi = models.BooleanField(default=False)
    
    def __str__(self):
        return self.sarlavha
    


    
