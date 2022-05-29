from .services import ProductService
from protos import products_pb2_grpc


def grpc_handlers(server):
    products_pb2_grpc.add_productfuncsServicer_to_server(
        ProductService.as_servicer(), server)
