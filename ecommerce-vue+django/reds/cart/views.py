from urllib import response
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
from protos import cart_pb2,cart_pb2_grpc
# Create your views here.

@api_view(['POST'])
def createcart(request):
    data = request.data
    cartdata=cartserializer(data=data)
    with grpc.insecure_channel("localhost:50053") as channel:
        stub=cart_pb2_grpc.cartopsStub(channel)
        if(cartdata.is_valid(raise_exception=True)):
            response=stub.createcart(cart_pb2.createRequest(req=cartdata.data))
            serializer=cartserializer(data=response.req)
            print(serializer)
            if(serializer.is_valid(raise_exception=True)):
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    # print(data)
    # serializer = cartserializer(data=data)
    # print(serializer)
    # if serializer.is_valid():
    #     serializer.save()
    


@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def updatecart(request):
    print("I am here")
    data=request.data
    data["username"] = request.user.get_username()
    req=cartserializer(data=data)
    req.is_valid(raise_exception=True)
    print(req.data)
    with grpc.insecure_channel("localhost:50053") as channel:
        stub=cart_pb2_grpc.cartopsStub(channel)
        response = stub.updatecart(cart_pb2.createRequest(req=req.data))
        print(response)
        return Response(response.response)
        
    # print("++++++++++++++++++++++",data)
    # data.username=
    # print("I am here")
    # try:
    #     print("========================",request.user.get_username(),"===================================")
    #     obj1 = cart.objects.get(username=request.user.get_username())
    #     obj=mycartserializer(obj1)
    #     print(obj.data)
    #     # data["items"]=obj.data["items"]

    #     print("+++++++++",data["items"])
    #     print("++++++++++",obj1.delete())
    #     serializer = cartserializer(data=data)
    # # print("---------------",obj)
    # # # serializer=cartserializer(instance=obj,data=obj)
    #     if(serializer.is_valid()):
    #         print('It is valid')
    #         serializer.save()
    #         return Response(status=status.HTTP_200_OK)
    #     else:
    #         return Response(status=status.HTTP_404_NOT_FOUND)
    # except Exception as e:
    #     print("================\nError:=========",e)
    #     return Response(status=status.HTTP_404_NOT_FOUND)
    
    
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
        with grpc.insecure_channel("localhost:50053") as channel:
            stub = cart_pb2_grpc.cartopsStub(channel)
            print(request.user.get_username())
            username=request.user.get_username()
            response = stub.getCart(cart_pb2.getRequest(username=username))
            print(request.user.get_username())
            serializer=mycartserializer(response.response)
            return Response(serializer.data)
        # cartobj = cart.objects.get(username=request.user.get_username())
        # print(cartobj)
        # # serializer = mycartserializer(cartobj,many=True)
        # serializer = mycartserializer(cartobj)
        # print(serializer.data)
        # #print(serializer.data)

        # return Response(serializer.data)    




