from django.shortcuts import (get_object_or_404, render,HttpResponseRedirect)
from rest_framework import serializers
from .models import Product,cart
from django_grpc_framework import proto_serializers
from protos import cart_pb2


class ProductSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = Product
        proto_class=cart_pb2.product_
        fields = [
             "_id",
            "name",
            "get_absolute_url",
            "description",
            "price",
            "get_image",
            "get_thumbnail",
            "quantity",
        ]

class cartserializer(proto_serializers.ModelProtoSerializer):
    items=ProductSerializer(many=True)
    class Meta:
        model=cart
        proto_class = cart_pb2.cart
        fields=[
            "username",
            "items",
        ]
    def create(self,validated_data):
        items_data=validated_data.pop('items')
        # print("+++++++++++++++++------+++++++++++++",items_data)
        Cart=cart.objects.create(**validated_data)
        # print("++++++++++++++++++++++++++++++++++",Cart)
        try:
            for item_data in items_data:
                Product.objects.create(username=Cart,**item_data)
        except Exception as e:
            print(e)
        return Cart
    # def update(self,username,validated_data):
    #     items_data=validated_data.pop('items')
    #     print("+++++++++++++++++------+++++++++++++",items_data)
    #     Cart=cart.objects.get(username=username)
    #     print("++++++++++++++++++++++++++++++++++",Cart)
    #     try:
    #         for item_data in items_data:
    #             Product.objects.create(username=Cart,**item_data)
    #     except Exception as e:
    #         print(e)
    #     return Cart


class myProductSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = Product
        proto_class = cart_pb2.product_
        fields = [
             "_id",
            "name",
            "get_absolute_url",
            "description",
            "price",
            "get_image",
            "get_thumbnail",
            "quantity",
        ]


class mycartserializer(proto_serializers.ModelProtoSerializer):
    items=myProductSerializer(many=True)
    class Meta:
        model=cart
        proto_class = cart_pb2.cart
        fields=[
            "username",
            "items",
        ]
