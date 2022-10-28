from datetime import datetime
from email.policy import default
from tkinter import image_names
from django.db import models
from .choices import generos

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser

#Table departament (departamentos)
class Departament (models.Model):
    Name = models.CharField(max_length=50)

    def __str__(self):
        return self.Name
#Table Locaties (localidades o ciudades)
class Locaties(models.Model):
    Fk_departament = models.ForeignKey(Departament, on_delete=models.CASCADE)
    Name = models.CharField(max_length=30)

    def __str__(self):
        return self.Name







class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        email = self.email.normalize(email)

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
            raise ValueError("Super user has to have is_staff being True")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Super user has to have is_superuser being True")

        return self.create_superuser(email=email, password=password,**extra_fields)



#Table Users (usuarios)
class Users (AbstractUser):
    Id_user = models.BigAutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    CellPhone = models.TextField()
    Email = models.TextField(max_length=90,unique=True)
    Password = models.CharField(max_length=20, null=True, default='password')
    Rol = models.CharField(default='[ROLE_USUARIO]',max_length=20)
    image = models.ImageField()
    Condition = models.CharField(default=1, max_length=1)

    objects = CustomUserManager()
    USERNAME_FIELD = "Email"
    REQUIRED_FIELDS = ['Name']

    def name_User(self):
        return "{} {}".format(self.Name,self.LastName)

    def __str__(self):
        return self.name_User()






#Table Tattoo artist (Tatuadores)
class Tattoo_artist (models.Model):
    Id_artist = models.BigAutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    Cellphone = models.TextField()
    Departament = models.ForeignKey(Departament, on_delete=models.CASCADE)
    Locaties = models.ForeignKey(Locaties, on_delete=models.CASCADE)
    Direction = models.TextField()
    Email = models.TextField(max_length=90)
    Experience = models.CharField(max_length=3)
    Description=models.TextField(max_length=150,blank=True,default='')
    Password = models.TextField(max_length=20)
    Rol = models.CharField(default='[ROLE_TATUADOR]',max_length=20)
    image = models.ImageField()
    Condition = models.CharField(default='A', max_length=1)

    def name_artist(self):
        return "{} {}".format(self.Name,self.LastName)

    def __str__(self):
        return self.name_artist()

#Table quotes (citas)
class Quotes(models.Model):
    Id_quotes = models.BigAutoField(primary_key=True)
    Tattoo_artist = models.ForeignKey(Tattoo_artist, on_delete=models.CASCADE)
    User = models.ForeignKey(Users, on_delete=models.CASCADE)
    Date = models.DateField()
    Time = models.TimeField()
    Img = models.ImageField()
    Description = models.CharField(max_length=150, blank=False, default='')

#Table brifcase_artist (portafolio tatuador)
class briefcase_artist(models.Model):
    Id_briefcase = models.BigAutoField(primary_key=True)
    Date_publication = models.DateTimeField(default=datetime.now())
    Tattoo_artist = models.ForeignKey(Tattoo_artist, on_delete=models.CASCADE)
    Img = models.ImageField()
    Description = models.TextField(max_length=150,blank=True,default='')

#Table likes (me gustas)
class likes(models.Model):
    Id_likes = models.BigAutoField(primary_key=True)
    Tattoo_artist = models.ForeignKey(Tattoo_artist, on_delete=models.CASCADE)
    Counter_likes = models.IntegerField()

