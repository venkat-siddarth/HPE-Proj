#from unicodedata import category
import grpc
from google.protobuf import empty_pb2
from protos import products_pb2
from django_grpc_framework.services import Service
from django.db.models import Q
from .models import Category,Product
from .serializers import CategorySerializer, ProductSerializer

class ProductService(Service):
    def getproductlist(self,request,context):
        products = list(Product.objects.all()[0:4])
        serializer = ProductSerializer(products, many=True)
        # serializer.is_valid(raise_exeception=True)
        # serializer.save()
        print(serializer.message)
        return products_pb2.latestProductsResponse(product=serializer.message)
    def getproductdetails(self,request,context):
        print(request.categoryslug,request.productslug)
        try:
            serializer=ProductSerializer(Product.objects.filter(category__slug=request.categoryslug).get(slug=request.productslug))
            return products_pb2.productDetailsResponse(product=serializer.message)
        except Product.DoesNotExist:
            self.context.abort(grpc.StatusCode.NOT_FOUND,'Product or Category not found!')

    def id(self,request,context):
        #print(request.id)
        try:
            serializer=ProductSerializer(Product.objects.get(id=request.id))
            return products_pb2.prodIDResponse(product=serializer.message)
        except Product.DoesNotExist:
            #print("Doest")
            return self.context.abort(grpc.StatusCode.NOT_FOUND,'Product or Category not found!')
    def getcategorylist(self,request,context):
        try:
            serializer = CategorySerializer(
                Category.objects.get(slug=request.categoryslug))
            return products_pb2.CategoryProductsResponse(category=serializer.message)
        except Category.DoesNotExist:
            return self.context.abort(grpc.StatusCode.NOT_FOUND,
                               'Product or Category not found!')
    def search(self,request,context):
        query=request.query;
        if query:
            products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
            serializer = ProductSerializer(products, many=True)
            return products_pb2.searchResponse(product=serializer.message)
        else:
            return empty_pb2.Empty()


