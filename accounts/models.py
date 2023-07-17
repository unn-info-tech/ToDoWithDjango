from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.

# in English -  CustomUserManager
class MaxsusFoydalanuvchiBoshqaruvchisi(BaseUserManager):

    def create_foydalanuvchi(self, pochta, parol=None, **extra_fields):
        if not pochta:
            raise ValueError('Pochtaning kriting')
        pochta = self.normalize_email(pochta)
        foydalanuvchi = self.model(email=pochta, **extra_fields)
        foydalanuvchi.set_password(parol)
        foydalanuvchi.save(using=self._db)
        return foydalanuvchi

    def create_superfoydalanuvchi(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

# in uzbek - MaxsusFoydalanuvchi