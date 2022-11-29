from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
# from accounts import models 


# Create your models here.

Users = get_user_model()


class Quotes(models.Model):
    id_quotes = models.BigAutoField(primary_key=True)
    date = models.DateField()
    time = models.TimeField()
    img = models.CharField(max_length=500)
    description = models.CharField(max_length=150, blank=False, default='')
    userID = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="perfilUser")
    artist_tattoo = models.ForeignKey(Users, on_delete=models.CASCADE, related_name= "perfilTattoo")
    isActive = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.id_quotes