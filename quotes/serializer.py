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

class DeleteQuotes(serializers.ModelSerializer):
    class Meta:
        model = Quotes
        fields = '__all__'


class UpdateQuotes(serializers.ModelSerializer):
    isActive = serializers.BooleanField()
    class Meta:
        model = Quotes
        fields = ['isActive']

    def update(self, instance, validated_data):
        instance.isActive = validated_data.get('isActive',instance.isActive)
        instance.save()
        return instance

        
        