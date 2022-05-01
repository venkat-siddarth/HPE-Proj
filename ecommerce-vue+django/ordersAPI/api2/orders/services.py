import stripe
import grpc
from google.protobuf import empty_pb2
from django_grpc_framework.services import Service
from django.conf import settings
from .models import Order,OrderItem
from .serializers import OrderSerializer, MyOrderSerializer
from protos import orders_pb2
class OrderService(Service):
    def checkout(self,request,context):
        #print(req
        serializer = OrderSerializer(message=request.data)
        print(serializer.is_valid())
        if serializer.is_valid():
            # serializer.data["username"]=request.user.get_username()
            # serializer.commit()
            # print(serializer.data)
            #print(serializer.message)
            stripe.api_key = settings.STRIPE_SECRET_KEY
            paid_amount = sum(item.get('price')
                              for item in serializer.validated_data['items'])
            try:
                charge = stripe.Charge.create(
                amount=int(paid_amount * 100),
                currency='USD',
                description='Charge from Redstone',
                source=serializer.validated_data['stripe_token']
                )
                #return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                pass
           # print("Hello World")
            serializer.save(paid_amount=paid_amount)
            return orders_pb2.checkoutResponse(data=serializer.message)
    
    def getOrderList(self,request,context):
        try:
           # print("fsdf",request.user)
            orders = Order.objects.filter(username=request.user)
            #print(orders)
            serializer = MyOrderSerializer(orders, many=True)
            #print("F",serializer.message)
            return orders_pb2.getOrderListResponse(data=serializer.message)
        except Order.DoesNotExist:
            self.context.abort(grpc.StatusCode.NOT_FOUND,'Order not found!')
            return empty_pb2.Empty()




