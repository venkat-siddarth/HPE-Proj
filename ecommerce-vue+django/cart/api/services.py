
from logging import raiseExceptions
from django.conf import settings
#from django.contrib.auth.models import User
#from django.http import Http404
from django.shortcuts import render
from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
import grpc 
from google.protobuf import empty_pb2
from django_grpc_framework.services import Service
from .models import Product,cart
from .serializers import cartserializer,mycartserializer,myProductSerializer,ProductSerializer
from protos import cart_pb2,cart_pb2_grpc
class cartservices(Service):
    def createcart(self,request,context):
        # data = request.data
        # print(data)
        serializer = cartserializer(message=request.req)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return cart_pb2.createResponse(req=serializer.message)

    def updatecart(self,request,context):
        print("========================", request.req.username,
              "===================================")
        try:
            
            obj1 = cart.objects.get(username=request.req.username)
            obj = mycartserializer(obj1)
            print(obj)
        # data["items"]=obj.data["items"]

            # print("+++++++++", data["items"])
            
            serializer = cartserializer(message=request.req)
            print("+++---",serializer.is_valid(raise_exception=True))
    # print("---------------",obj)
    # # serializer=cartserializer(instance=obj,data=obj)
            if(serializer.is_valid( raise_exception=True)):
                print("++++++++++", obj1.delete())
                print('It is valid')
                serializer.save()
                return cart_pb2.updateResponse(response=str(status.HTTP_200_OK))
            else:
                return cart_pb2.updateResponse(response=str(status.HTTP_404_NOT_FOUND))
        except Exception as e:
            print("================Error:=========", e)
            return cart_pb2.updateResponse(response=str(status.HTTP_404_NOT_FOUND))

    def getCart(self,request,context):
        print(request)
        cartobj = cart.objects.get(username=request.username)
        # serializer = mycartserializer(cartobj,many=True)
        serializer = mycartserializer(cartobj)
        # print(serializer.data)
        print(serializer.message)
        return cart_pb2.getResponse(response=serializer.message)
