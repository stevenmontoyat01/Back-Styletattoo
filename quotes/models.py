from django.db import models

# Create your models here.

class Quotes(models.Model):
    Id_quotes = models.BigAutoField(primary_key=True)
    Date = models.DateField()
    Time = models.TimeField()
    Img = models.ImageField()
    Description = models.CharField(max_length=150, blank=False, default='')


# Tattoo_artist = models.ForeignKey(Tattoo_artist, on_delete=models.CASCADE)
# User = models.ForeignKey(Users, on_delete=models.CASCADE)