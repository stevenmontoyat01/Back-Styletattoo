from rest_framework import status,generics,mixins
from rest_framework.response import Response
from rest_framework.request import Request

from .serializer import *
from .models import *



# Create your views here.

#-------------------------------------------------------------------------------------------#
#-----------------------API CITAS METHODS GET POST PUT DELETE-------------------------------#
#-------------------------------------------------------------------------------------------#



class ViewsQuotes(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,):
    serializer_class = RegisterQuotes
    queryset = Quotes.objects.all()
    
    def get(self, request: Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request: Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)




# class ViewsQuotes(generics.GenericAPIView):
#     permission_classes = []
#     serializer_class = RegisterQuotes

#     def post(self, request:Request):
#         data = request.data
#         serializer = self.serializer_class(data=data)


#         if serializer.is_valid():
#             serializer.save()
#             response = {
#                 "massage":"cita registrada",
#                 "data" : serializer.data
#             }

#             return Response (data=response, status= status.HTTP_201_CREATED)

#         return Response (data=serializer.errors, status= status.HTTP_201_CREATED)