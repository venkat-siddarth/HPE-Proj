import stripe
from django.conf import settings
#from django.contrib.auth.models import User
#from django.http import Http404
from django.shortcuts import render
from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Order, OrderItem
from .serializers import OrderSerializer, MyOrderSerializer

@api_view(['POST'])
# @authentication_classes([authentication.TokenAuthentication])
# @permission_classes([permissions.IsAuthenticated])
def checkout(request):
    print("++++++",request.data)
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        # serializer.data["username"]=request.user.get_username()
        # serializer.commit()
        # print(serializer.data)
        stripe.api_key = settings.STRIPE_SECRET_KEY
        paid_amount = sum(item.get('price') for item in serializer.validated_data['items'])
        try:
            charge = stripe.Charge.create(
                amount=int(paid_amount * 100),
                currency='USD',
                description='Charge from Redstone',
                source=serializer.validated_data['stripe_token']
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e :
            print(e)
        serializer.save(paid_amount=paid_amount,username=request.user.get_username())
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class OrdersList(APIView):
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
    def get(self, request, format=None):
        #print(request.username)
        orders = Order.objects.filter(username=request.user)
        #print(orders)
        serializer = MyOrderSerializer(orders, many=True)
        #print(serializer.data)
        return Response(serializer.data)