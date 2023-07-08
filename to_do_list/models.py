from django.db import models
from django.utils.timezone import now
class Foydalanuvchi(models.Model):
    ism = models.CharField(max_length=25)
    familiya = models.CharField(max_length=25)
    pochta = models.EmailField()
    dob = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.ism} {self.familiya}"

    
class Vazifalar(models.Model):
    foydalanuvchi = models.ForeignKey(Foydalanuvchi, on_delete=models.CASCADE)
    sarlavha = models.CharField(max_length=200)
    haqida = models.TextField()
    bajarildi = models.BooleanField(default=False)

    def __str__(self):
        return self.sarlavha