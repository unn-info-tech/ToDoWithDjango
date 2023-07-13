from django.contrib import admin
from .models import VazifaModel, FoydalanuvchiModel, UquvchiModel

# Register your models here.
admin.site.register(FoydalanuvchiModel)
admin.site.register(VazifaModel)
admin.site.register(UquvchiModel)

