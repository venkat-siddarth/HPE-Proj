from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
from rest_framework import serializers
from .models import Product,cart
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
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
class cartserializer(serializers.ModelSerializer):
    items=ProductSerializer(many=True)
    class Meta:
        model=cart
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

class myProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
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
class mycartserializer(serializers.ModelSerializer):
    items=myProductSerializer(many=True)
    class Meta:
        model=cart
        fields=[
            "username",
            "items",
        ]