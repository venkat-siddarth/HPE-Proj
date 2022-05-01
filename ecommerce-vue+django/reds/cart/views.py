from django.conf import settings
#from django.contrib.auth.models import User
#from django.http import Http404
from django.shortcuts import render
from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
import grpc
from .serializers import cartSerializer,ProductSerializer
from .models import Product, cart

# Create your views here.

@api_view(['POST'])
def createCart(request):
    data = request.data
    serializer = cartSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

def addtocart(request):
    data=request.data
    serializer=cartSerializer(data=data)
    if serializer.is_valid():
        # serializer.data["username"]=request.user.get_username()
        # serializer.commit()
        serializer.save(username=request.data["username"])
        print("Successfull")  
        return Response(serializer.data,status=status.HTTP_201_CREATED)






