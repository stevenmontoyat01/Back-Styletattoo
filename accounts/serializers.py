#Libraries
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import ValidationError
from rest_framework import status


from .models import Users

#_____________________________________________#
# || R E G I S T R O  ||   U S U A R I O S  ||
class SignUpSzer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=45)
    first_name = serializers.CharField(max_length=45)
    last_name = serializers.CharField(max_length=45)
    email = serializers.CharField(max_length=90)
    password = serializers.CharField(min_length=8, write_only=True)



    class Meta:
        model= Users
        fields= ['username','first_name', 'last_name','email','password','rol','is_active']

    def validate(self, attrs):
        email_exists = Users.objects.filter(email=attrs["email"]).exists()

        if email_exists:
            raise ValidationError({"response":"email se encuentra en uso","status":status.HTTP_200_OK})
        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = super().create(validated_data)
        user.set_password(password)
        user.save()

        Token.objects.create(user=user)

        return user
    
