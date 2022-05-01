from rest_framework import serializers
from .models import Category,Product
from django_grpc_framework import proto_serializers
from protos import products_pb2
class ProductSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model=Product
        proto_class=products_pb2.product
        fields=[
            "id",
            "name",
            "get_absolute_url",
            "description",
            "price",
            "get_image",
            "get_thumbnail",
        ]


class CategorySerializer(proto_serializers.ModelProtoSerializer):
    products = ProductSerializer(many=True)
    class Meta:
        model = Category
        proto_class = products_pb2.category
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "products",
        )
