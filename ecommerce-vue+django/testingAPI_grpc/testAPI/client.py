import grpc
from protos import products_pb2,products_pb2_grpc;
with grpc.insecure_channel("localhost:50051") as channel:
    stub = products_pb2_grpc.productfuncsStub(channel)
    response=stub.getproductlist(products_pb2.latestProductsRequest())
    print(type(response.product[0]))

