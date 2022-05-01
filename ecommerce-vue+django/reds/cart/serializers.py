from rest_framework import serializers
from .models import Product,cart
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "get_absolute_url",
            "description",
            "price",
            "get_image",
            "get_thumbnail",
        ]
class cartSerializer(serializers.ModelSerializer):
    items=ProductSerializer(many=True)
    class Meta:
        model=cart
        fields=(
            "username",
        )
    def create(self,validated_data):
        items_data=validated_data.pop('items')
        Cart=cart.create(**validated_data)
        try:
            for item_data in items_data:
                Product.objects.create(username=Cart,**item_data)
        except Exception as e:
            print(e)
        return cart

