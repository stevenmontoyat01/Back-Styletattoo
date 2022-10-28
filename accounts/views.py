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
            response = {
                "message" : "login sucessful",
                "token":user.auth_token.key,
                "info_token" : tokens
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