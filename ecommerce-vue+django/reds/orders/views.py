import stripe
from django.conf import settings
#from django.contrib.auth.models import User
#from django.http import Http404
from django.shortcuts import render

from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
import grpc
from protos import orders_pb2,orders_pb2_grpc;
from .models import Order, OrderItem
from .serializers import OrderSerializer, MyOrderSerializer
import os
@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def checkout(request):
    request.data["username"]=request.user.get_username();
    print(request.data)
    # with grpc.insecure_channel("localhost:50052") as channel:
    orders_host = os.getenv("ORDERS_HOST", "localhost")
    with grpc.insecure_channel(f"{orders_host}:50052") as channel:
        stub = orders_pb2_grpc.ordersfuncsStub(channel)
        data=OrderSerializer(request.data)
        print(data.data)
        response=stub.checkout(orders_pb2.checkoutRequest(data=data.data))
        print("++++++++++++++++++",response)
        serializer=OrderSerializer(response.data)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    # print("++++++",request.data)
    # serializer = OrderSerializer(data=request.data)
    # if serializer.is_valid():
    #     # serializer.data["username"]=request.user.get_username()
    #     # serializer.commit()
    #     # print(serializer.data)
    #     stripe.api_key = settings.STRIPE_SECRET_KEY
    #     paid_amount = sum(item.get('price') for item in serializer.validated_data['items'])
    #     try:
    #         charge = stripe.Charge.create(
    #             amount=int(paid_amount * 100),
    #             currency='USD',
    #             description='Charge from Redstone',
    #             source=serializer.validated_data['stripe_token']
    #         )
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     except Exception as e :
    #         print(e)
    #     serializer.save(paid_amount=paid_amount,username=request.data["username"])
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)

class OrdersList(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, format=None):
        #print("sdfsdf",request.user.get_username())
        # with grpc.insecure_channel("localhost:50052") as channel:
        orders_host = os.getenv("ORDERS_HOST", "localhost")
        with grpc.insecure_channel(f"{orders_host}:50052") as channel:
            stub = orders_pb2_grpc.ordersfuncsStub(channel)
            try:
                
                response=stub.getOrderList(orders_pb2.getOrderListRequest(user=request.user.get_username()))
            except Exception as e:
                print(e)
            #print("++++",response)
            serializer=MyOrderSerializer(response.data,many=True)
            #print("f",serializer)
            return Response(serializer.data)

        # orders = Order.objects.filter(username=request.user)
        # #print(orders)
        # serializer = MyOrderSerializer(orders, many=True)
        # #print(serializer.data)
        # return Response(serializer.data)
