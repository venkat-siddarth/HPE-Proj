from rest_framework import serializers
from django_grpc_framework import proto_serializers
from .models import Order, OrderItem
from protos import orders_pb2
#from products.serializers import ProductSerializer

class MyOrderItemSerializer(proto_serializers.ModelProtoSerializer):    
    class Meta:
        model = OrderItem
        proto_class=orders_pb2.orderItem
        fields = (
            "price",
            "product",
            "quantity",
        )



class MyOrderSerializer(proto_serializers.ModelProtoSerializer):
    items = MyOrderItemSerializer(many=True)

    class Meta:
        model = Order
        proto_class=orders_pb2.order
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "address",
            "zipcode",
            "place",
            "phone",
            "stripe_token",
            "items",
            "paid_amount"
        )


class OrderItemSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = OrderItem
        proto_class = orders_pb2.orderItem
        fields = (
            "price",
            "product",
            "quantity",
        )


class OrderSerializer(proto_serializers.ModelProtoSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        proto_class = orders_pb2.order
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "address",
            "zipcode",
            "place",
            "phone",
            "stripe_token",
            "items",
        )
    
    def create(self, validated_data):
        #print(validated_data)
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        try:
            for item_data in items_data:
         #       print(item_data)
                OrderItem.objects.create(order=order, **item_data)
        except Exception as e:
            print(e)
        return order
