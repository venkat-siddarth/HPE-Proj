from django.http import Http404
from django.db.models import Q
from rest_framework.decorators import api_view
import grpc
import os
from protos import products_pb2,products_pb2_grpc;
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductSerializer,CategorySerializer
from .models import Product,Category


# Create your views here.
class LatestProductList(APIView):
    def get(self,request,format=None):
        products_rest_host = os.getenv("PRODUCTS_GRPC_HOST","localhost")
        with grpc.insecure_channel(f"{products_rest_host}:50051") as channel:
            stub = products_pb2_grpc.productfuncsStub(channel)
            response=stub.getproductlist(products_pb2.latestProductsRequest())
            serializer=ProductSerializer(response.product,many=True)
            print(serializer.data)
            return Response(serializer.data)


class ProductDetail(APIView):
    def get(self,request,category_slug,product_slug,format=None):
        products_rest_host = os.getenv("PRODUCTS_GRPC_HOST", "localhost")
        with grpc.insecure_channel(f"{products_rest_host}:50051") as channel:
            stub = products_pb2_grpc.productfuncsStub(channel)
            response=stub.getproductdetails(products_pb2.productDetailsRequest(categoryslug=category_slug,productslug=product_slug))
           # print(response)
            serializer=ProductSerializer(response.product)
          #  print(serializer.data)
            return Response(serializer.data)
        # print("category_slug,product_slug")
        # product=self.get_object(category_slug,product_slug)
        # serializer=ProductSerializer(product)
        # print(serializer)
        # return Response(serializer.data)

class ProductId(APIView):
    def get(self,request,id,format=None):
        # with grpc.insecure_channel("localhost:50051") as channel:
        products_rest_host = os.getenv("PRODUCTS_GRPC_HOST", "localhost")
        with grpc.insecure_channel(f"{products_rest_host}:50051") as channel:
            stub = products_pb2_grpc.productfuncsStub(channel)
            response=stub.id(products_pb2.prodIDRequest(id=id))
           # print(response)
            serializer=ProductSerializer(response.product)
          #  print(serializer.data)
            return Response(serializer.data)
        # print(id)
        # product=self.get_object(id)
        # serializer=ProductSerializer(product)
        # return Response(serializer.data)
    

class CategoryDetail(APIView):

    def get(self, request, category_slug, format=None):
        #  with grpc.insecure_channel("localhost:50051") as channel:
        products_rest_host = os.getenv("PRODUCTS_GRPC_HOST", "localhost")
        with grpc.insecure_channel(f"{products_rest_host}:50051") as channel:
            stub = products_pb2_grpc.productfuncsStub(channel)
            response=stub.getcategorylist(products_pb2.CategoryProductsRequest(categoryslug=category_slug))
           # print(response)
            serializer=CategorySerializer(response.category)
          #  print(serializer.data)
            return Response(serializer.data)


@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')
    # with grpc.insecure_channel("localhost:50051") as channel:
    products_rest_host = os.getenv("PRODUCTS_GRPC_HOST", "localhost")
    with grpc.insecure_channel(f"{products_rest_host}:50051") as channel:
        stub = products_pb2_grpc.productfuncsStub(channel)
        response=stub.search(products_pb2.searchRequest(query=query))
        print(response.product)
        serializer=ProductSerializer(response.product,many=True)
        print(serializer.data)
        return Response(serializer.data)
