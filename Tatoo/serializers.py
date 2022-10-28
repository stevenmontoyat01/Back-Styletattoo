#Libraries
import email
from imaplib import _Authenticator
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import ValidationError
from .models import Users,Tattoo_artist,Quotes,Departament,Locaties,likes,briefcase_artist


#METHOD POST

#FORMULARIO REGISTROS CITAS
class QuotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quotes
        fields= "__all__"

# FORMULATIO REGISTRO PORTAFOLIO
class Briefcase_ArtistSerializers(serializers.ModelSerializer):
    class Meta:
        model= briefcase_artist
        fields=(
            'tatuador',
            'imagen',
            'descripcion'
        )

#------------------------------------------------------------------------------------------
# FORMULARIOS  REGISTROS USUARIOS

class UsersModelSerializers(serializers.ModelSerializer):
    Name = serializers.CharField(max_length=50)
    LastName = serializers.CharField(max_length=50)
    Password = serializers.CharField(max_length=20)
    Email = serializers.CharField(max_length=90)
    CellPhone = serializers.CharField(max_length=50)

    class Meta:
        model= Users
        fields= [
            "Name",
            "LastName",
            "CellPhone",
            "Password",
            "Email"
        ]

    def validate(self, attrs):
        email_exists = Users.objects.filter(Email=attrs["Email"]).exists()

        if email_exists:
            raise ValidationError("El Correo ya se encuentra en uso")
        return super().validate(attrs)
    
    # def create(self, validated_data):
    #     password = validated_data.pop("password")

    #     user = super().create(validated_data)
    #     user.set_password(password)
    #     user.save()

    #     Token.objects.create(user=user)

    #     return user


#--------------------------------------------------------------------------------------------
# FORMULARIOS REGISTROS TATUADORES
class Tattoo_ArtistSerializers(serializers.ModelSerializer):
    class Meta:
        model= Tattoo_artist
        fields= "__all__"
        

#-------------------------------------------------------------------------------------------
# REGISTRO DEPARTAMENTOS
class DepartamentsSerializers(serializers.ModelSerializer):

    class Meta:
        model = Departament
        fields= "__all__"
#REGISTRO LOCALIDADES
class LocatiesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Locaties
        fields = "__all__"


#METHOD GET

class GetUsers(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields= "__all__"

class GetArtist(serializers.ModelSerializer):

    class Meta:
        model = Tattoo_artist
        model = (
            'Id_artist',
            'Name'
        )