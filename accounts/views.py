from django.shortcuts import render
from .serializers import SignUpSzer

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.request import Request 


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

        # return Response (
        #     data={"message":"error in the request","status":status.HTTP_400_BAD_REQUEST}, 
        #     status=status.HTTP_400_BAD_REQUEST)
        




# class Login(APIView):
#     permission_classes = []

#     def post(self, request:Request):
#         email = request.data.get('Email'),
#         password = request.data.get('Password')

#         user = authenticate(Email = email, Password = password)

#         if user is not None:
#             tokens = create_jwt_pair_for_user(user)
#             response = {
#                 "message" : "login sucessful",
#                 "token" : user.auth_token.key 
#             }
#             return Response(data = response, status = status.HTTP_200_OK)
            
#         else:
#             return Response(data = {"messsage":"invalid email or password"})

#     def get(self, request : Request):
#         content = {
#             "user":str(request.user),
#             "auth":str(request.auth) 
#         }

#         return Response(data= content, status= status.HTTP_200_OK)