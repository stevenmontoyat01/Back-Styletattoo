from rest_framework import serializers
from rest_framework.validators import ValidationError
from quotes.models import Quotes
from django.contrib.auth.models import User
from rest_framework import status

from .models import Quotes





class RegisterQuotes(serializers.ModelSerializer):
    class Meta:
        model = Quotes
        fields = ['date','time','img','description','userID','artist_tattoo']



# class RegisterQuotes(serializers.ModelSerializer):
#     date = serializers.DateField()
#     time = serializers.TimeField()
#     img = serializers.CharField(max_length = 100)
#     description = serializers.CharField(max_length = 150)
#     artist_tattoo = serializers.IntegerField()
#     user = serializers.IntegerField()

#     class Meta:
#         model = Quotes
#         fields = ['date','img','time','description','artist_tattoo','user',]

class DeleteQuotes(serializers.ModelSerializer):
    class Meta:
        model = Quotes
        fields = '__all__'
        