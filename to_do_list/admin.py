from django.contrib import admin
from .models import Vazifalar, Foydalanuvchi, UquvchiModel

# Register your models here.
admin.site.register(Foydalanuvchi)
admin.site.register(Vazifalar)
admin.site.register(UquvchiModel)

