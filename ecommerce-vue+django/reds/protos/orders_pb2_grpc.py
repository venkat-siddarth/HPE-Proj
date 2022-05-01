# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import orders_pb2 as orders__pb2


class ordersfuncsStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.checkout = channel.unary_unary(
                '/ordersfuncs/checkout',
                request_serializer=orders__pb2.checkoutRequest.SerializeToString,
                response_deserializer=orders__pb2.checkoutResponse.FromString,
                )
        self.getOrderList = channel.unary_unary(
                '/ordersfuncs/getOrderList',
                request_serializer=orders__pb2.getOrderListRequest.SerializeToString,
                response_deserializer=orders__pb2.getOrderListResponse.FromString,
                )


class ordersfuncsServicer(object):
    """Missing associated documentation comment in .proto file."""

    def checkout(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getOrderList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ordersfuncsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'checkout': grpc.unary_unary_rpc_method_handler(
                    servicer.checkout,
                    request_deserializer=orders__pb2.checkoutRequest.FromString,
                    response_serializer=orders__pb2.checkoutResponse.SerializeToString,
            ),
            'getOrderList': grpc.unary_unary_rpc_method_handler(
                    servicer.getOrderList,
                    request_deserializer=orders__pb2.getOrderListRequest.FromString,
                    response_serializer=orders__pb2.getOrderListResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ordersfuncs', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ordersfuncs(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def checkout(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ordersfuncs/checkout',
            orders__pb2.checkoutRequest.SerializeToString,
            orders__pb2.checkoutResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getOrderList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ordersfuncs/getOrderList',
            orders__pb2.getOrderListRequest.SerializeToString,
            orders__pb2.getOrderListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
