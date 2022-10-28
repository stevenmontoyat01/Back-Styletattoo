from django.db import models

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
# Create your models here.



class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)

        user = self.model(
            email = email,
            **extra_fields
        )
        user.set_password(password)
        user.save()

        return user 

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError("El super usuario debe tener (is_staff) siendo Verdadero")


        if extra_fields.get('is_superuser') is not True:
            raise ValueError("El super usuario debe tener (is_superuser) siendo Verdadero")
        return self.create_user(email=email, password=password,**extra_fields)


class Users(AbstractUser):
    username = models.CharField(max_length=45)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=90 ,unique=True)
    image = models.ImageField(default='https://i.postimg.cc/T2N5CnwK/perfil-Usuario-Anonim.png',)
    rol = models.CharField(max_length=20)
    is_active= models.CharField(default=1, max_length=1)


    objects = CustomUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username","first_name","last_name","rol"]


    def __str__(self):
        return self.name
