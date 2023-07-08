from django.db import models

class Foydalanuvchi(models.Model):
    ism = models.CharField(max_length=25)
    familiya = models.CharField(max_length=25)
    pochta = models.EmailField()

    def __str__(self):
        return f"{self.ism} {self.familiya}"

    
class Vazifalar(models.Model):
    foydalanuvchi = models.ForeignKey(Foydalanuvchi, on_delete=models.CASCADE)
    sarlavha = models.CharField(max_length=200)
    haqida = models.TextField()
    bajarildi = models.BooleanField(default=False)

    def __str__(self):
        return self.title