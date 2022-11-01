import string
from django.shortcuts import render
from .serializers import SignUpSzer

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.request import Request 
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from .tokens import create_jwt_pair_for_user
from rest_framework.permissions import IsAuthenticated

# Create your views here.
from django.views.generic import View
from .serializers import ChangePasswordSerializer
from .models import Users

class signUpView(generics.GenericAPIView):
    permission_classes = []
    serializer_class = SignUpSzer

    def post(self, request:Request):
        data = request.data
        serializer = self.serializer_class(data = data)

        if serializer.is_valid():
            serializer.save()
            response = {
                "massage":"Usuario Creado Con Exito",
                "data" : serializer.data
            }

            return Response (data=response, status= status.HTTP_201_CREATED)

        return Response (data=serializer.errors, status= status.HTTP_201_CREATED)
        


class Login(APIView):
    permission_classes = []

    def post(self, request:Request):
        email = request.data.get('email')
        password = request.data.get('password')
        print(email)
        user = authenticate(email=email,password=password)


        if user is not None:
            tokens = create_jwt_pair_for_user(user)

            info_user={
                "id": user.id,
                "first_name":user.first_name,
                "last_name":user.last_name,
                "cellphone":user.cellPhone,
                "image":user.image,
                "rol":user.rol,
                "activate":user.is_active,
            }

            authentication = {
                "jwt" : tokens,
                "token":user.auth_token.key,
            }

            response = {
                "message" : "login sucessful",
                "info":info_user,
                "authentication":authentication
            }
            return Response(data = response, status = status.HTTP_200_OK)
        else:
            return Response(data = {"messsage":"email o password invalido"},status=status.HTTP_401_UNAUTHORIZED)

    def get(self, request : Request):
        content = {
            "user":str(request.user),
            "auth":str(request.auth) 
        }

        return Response(data= content, status= status.HTTP_200_OK)



class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    model = Users
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():

            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)

            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Users_id(APIView):
    permission_classes = []

    def get(self,request:Request,token_id:string):
        user = self.request
        print (user)