from api.services import cartservices
from protos import cart_pb2_grpc

def grpc_handlers(server):
    cart_pb2_grpc.add_cartopsServicer_to_server(cartservices.as_servicer(),server)