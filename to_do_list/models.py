from django.db import models
from django.utils.timezone import now
from datetime import time


class FoydalanuvchiModel(models.Model):
    ism = models.CharField(max_length=25)
    familya = models.CharField(max_length=25)
    email = models.EmailField()

    def __str__(self):
        return f"{self.ism} {self.familya}"

    
class VazifaModel(models.Model):
    foydalanuvchi = models.ForeignKey(FoydalanuvchiModel, on_delete=models.CASCADE, default=1)
    sarlavha = models.CharField(verbose_name="vazifa", max_length=200)
    tuliq_malumot = models.TextField()
    tugatish_muddati = models.DateTimeField(null=True, blank=True)
    bajarildi = models.BooleanField(default=False)
    
    def __str__(self):
        return self.sarlavha
    

class UquvchiModel(models.Model):
    first_name = models.CharField(verbose_name="Ism", max_length=35)
    last_name = models.CharField(verbose_name="Familiya", max_length=23)

    
