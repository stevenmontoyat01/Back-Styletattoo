# Libraries
import re
from os import stat
from ast import Return
from http.client import ResponseNotReady

from unicodedata import name
from urllib import request, response

from django.contrib.auth import authenticate
from django.shortcuts import get_list_or_404

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework import status,generics,viewsets
from rest_framework.decorators import api_view, APIView
from rest_framework.decorators import action

from .tokens import User, create_jwt_pair_for_user

# Models and serializers
from . import models, serializers

#-------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------#

   #API GET DATA USERS
@api_view(http_method_names=["GET"])
def getUsers (request:Request):
    users = models.Users.objects.all()

    serializer = serializers.UsersModelSerializers(instance = users, many = True)

    return Response(data = serializer.data, status= status.HTTP_200_OK)

#API GET DATA USER WITCH ID_USER
@api_view(http_method_names=["GET"])
def getUser(request:Request , post_id:int):
    users = get_list_or_404(models.Users, pk=post_id)

    serializer = serializers.UsersModelSerializers(instance=users, many = True)

    response = {
        "massage" : "resulted",
        "data" : serializer.data ,
        "status" : status.HTTP_200_OK
    }

    return Response(data = response, status = status.HTTP_200_OK)
#eigsto
#API POST USERS
@api_view(http_method_names=["POST"])
def postUser (request:Request):
    users = models.Users.objects.all()

    if request.method == "POST":
        data = request.data

        serializer = serializers.UsersSerializers(data = data , many = True)

        if serializer.is_valid():
            serializer.save()

            response = {
                "massage": "create register of user",
                "data" : serializer.data
            }
            return Response(data = response, status= status.HTTP_201_CREATED )

        return Response(data = serializer.errors, status= status.HTTP_400_BAD_REQUEST)

class Login(APIView):
    permission_classes = []

    def post(self, request:Request):
        email = request.data.get('Email'),
        password = request.data.get('Password')

        user = authenticate(Email = email, Password = password)

        if user is not None:
            tokens = create_jwt_pair_for_user(user)
            response = {
                "message" : "login sucessful",
                "token" : user.auth_token.key 
            }
            return Response(data = response, status = status.HTTP_200_OK)
            
        else:
            return Response(data = {"messsage":"invalid email or password"})

    def get(self, request : Request):
        content = {
            "user":str(request.user),
            "auth":str(request.auth) 
        }

        return Response(data= content, status= status.HTTP_200_OK)

class signup(generics.GenericAPIView):
    permission_classes = []
    serializer_class = serializers.UsersModelSerializers

    def post(self, request:Request):
        data = request.data
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            response = {
                "massage":"user created exist",
                "data" : serializer.data
            }

            return Response (data=response, status= status.HTTP_201_CREATED)

        return Response (data=serializer.errors, status= status.HTTP_201_CREATED)

        # return Response (
        #     data={"message":"error in the request","status":status.HTTP_400_BAD_REQUEST}, 
        #     status=status.HTTP_400_BAD_REQUEST)
        

        

