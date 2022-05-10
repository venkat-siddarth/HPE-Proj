from django.conf import settings
#from django.contrib.auth.models import User
#from django.http import Http404
from django.shortcuts import render

from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
import grpc
from .serializers import cartserializer,ProductSerializer,mycartserializer
from .models import Product, cart

# Create your views here.

@api_view(['POST'])
def createcart(request):
    data = request.data
    print(data)
    serializer = cartserializer(data=data)
    print(serializer)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def updatecart(request):
    print("I am here")
    data=request.data
    data["username"] = request.user.get_username()
    # print("++++++++++++++++++++++",data)
    # data.username=
    print("I am here")
    try:
        print("========================",request.user.get_username(),"===================================")
        obj1 = cart.objects.get(username=request.user.get_username())
        obj=mycartserializer(obj1)
        print(obj.data)
        # data["items"]=obj.data["items"]

        print("+++++++++",data["items"])
        print("++++++++++",obj1.delete())
        serializer = cartserializer(data=data)
    # print("---------------",obj)
    # # serializer=cartserializer(instance=obj,data=obj)
        if(serializer.is_valid()):
            print('It is valid')
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        print("================\nError:=========",e)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    
    # print(obj)
    # print("---------------", obj)
    

class cart_(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, format=None):
        #print("sdfsdf",request.user.get_username())
        # with grpc.insecure_channel("localhost:50052") as channel:
        #     stub = orders_pb2_grpc.ordersfuncsStub(channel)
        #     try:
                
        #         response=stub.getOrderList(orders_pb2.getOrderListRequest(user=request.user.get_username()))
        #     except Exception as e:
        #         print(e)
        #     #print("++++",response)
        #     serializer=MyOrderSerializer(response.data,many=True)
        #     #print("f",serializer)
        #     return Response(serializer.data)

        # cartobj = cart.objects.filter()
        #print(orders)
        cartobj = cart.objects.get(username=request.user.get_username())
        print(cartobj)
        # serializer = mycartserializer(cartobj,many=True)
        serializer = mycartserializer(cartobj)
        print(serializer.data)
        #print(serializer.data)

        return Response(serializer.data)    




