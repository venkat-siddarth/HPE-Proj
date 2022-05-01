from orders.services import OrderService
from protos import orders_pb2_grpc


def grpc_handlers(server):
    orders_pb2_grpc.add_ordersfuncsServicer_to_server(OrderService.as_servicer(), server)
