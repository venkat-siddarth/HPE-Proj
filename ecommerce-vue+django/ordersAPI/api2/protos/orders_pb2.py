# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: orders.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0corders.proto\"=\n\torderItem\x12\r\n\x05price\x18\x01 \x01(\x01\x12\x0f\n\x07product\x18\x02 \x01(\x05\x12\x10\n\x08quantity\x18\x03 \x01(\x05\"\xe1\x01\n\x05order\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x12\n\nfirst_name\x18\x03 \x01(\t\x12\x11\n\tlast_name\x18\x04 \x01(\t\x12\r\n\x05\x65mail\x18\x05 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x06 \x01(\t\x12\x0f\n\x07zipcode\x18\x07 \x01(\t\x12\r\n\x05place\x18\x08 \x01(\t\x12\r\n\x05phone\x18\t \x01(\t\x12\x14\n\x0cstripe_token\x18\n \x01(\t\x12\x19\n\x05items\x18\x0b \x03(\x0b\x32\n.orderItem\x12\x13\n\x0bpaid_amount\x18\x0c \x01(\x01\"\'\n\x0f\x63heckoutRequest\x12\x14\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x06.order\"(\n\x10\x63heckoutResponse\x12\x14\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x06.order\"#\n\x13getOrderListRequest\x12\x0c\n\x04user\x18\x01 \x01(\t\",\n\x14getOrderListResponse\x12\x14\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x06.order2{\n\x0bordersfuncs\x12/\n\x08\x63heckout\x12\x10.checkoutRequest\x1a\x11.checkoutResponse\x12;\n\x0cgetOrderList\x12\x14.getOrderListRequest\x1a\x15.getOrderListResponseb\x06proto3')



_ORDERITEM = DESCRIPTOR.message_types_by_name['orderItem']
_ORDER = DESCRIPTOR.message_types_by_name['order']
_CHECKOUTREQUEST = DESCRIPTOR.message_types_by_name['checkoutRequest']
_CHECKOUTRESPONSE = DESCRIPTOR.message_types_by_name['checkoutResponse']
_GETORDERLISTREQUEST = DESCRIPTOR.message_types_by_name['getOrderListRequest']
_GETORDERLISTRESPONSE = DESCRIPTOR.message_types_by_name['getOrderListResponse']
orderItem = _reflection.GeneratedProtocolMessageType('orderItem', (_message.Message,), {
  'DESCRIPTOR' : _ORDERITEM,
  '__module__' : 'orders_pb2'
  # @@protoc_insertion_point(class_scope:orderItem)
  })
_sym_db.RegisterMessage(orderItem)

order = _reflection.GeneratedProtocolMessageType('order', (_message.Message,), {
  'DESCRIPTOR' : _ORDER,
  '__module__' : 'orders_pb2'
  # @@protoc_insertion_point(class_scope:order)
  })
_sym_db.RegisterMessage(order)

checkoutRequest = _reflection.GeneratedProtocolMessageType('checkoutRequest', (_message.Message,), {
  'DESCRIPTOR' : _CHECKOUTREQUEST,
  '__module__' : 'orders_pb2'
  # @@protoc_insertion_point(class_scope:checkoutRequest)
  })
_sym_db.RegisterMessage(checkoutRequest)

checkoutResponse = _reflection.GeneratedProtocolMessageType('checkoutResponse', (_message.Message,), {
  'DESCRIPTOR' : _CHECKOUTRESPONSE,
  '__module__' : 'orders_pb2'
  # @@protoc_insertion_point(class_scope:checkoutResponse)
  })
_sym_db.RegisterMessage(checkoutResponse)

getOrderListRequest = _reflection.GeneratedProtocolMessageType('getOrderListRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETORDERLISTREQUEST,
  '__module__' : 'orders_pb2'
  # @@protoc_insertion_point(class_scope:getOrderListRequest)
  })
_sym_db.RegisterMessage(getOrderListRequest)

getOrderListResponse = _reflection.GeneratedProtocolMessageType('getOrderListResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETORDERLISTRESPONSE,
  '__module__' : 'orders_pb2'
  # @@protoc_insertion_point(class_scope:getOrderListResponse)
  })
_sym_db.RegisterMessage(getOrderListResponse)

_ORDERSFUNCS = DESCRIPTOR.services_by_name['ordersfuncs']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ORDERITEM._serialized_start=16
  _ORDERITEM._serialized_end=77
  _ORDER._serialized_start=80
  _ORDER._serialized_end=305
  _CHECKOUTREQUEST._serialized_start=307
  _CHECKOUTREQUEST._serialized_end=346
  _CHECKOUTRESPONSE._serialized_start=348
  _CHECKOUTRESPONSE._serialized_end=388
  _GETORDERLISTREQUEST._serialized_start=390
  _GETORDERLISTREQUEST._serialized_end=425
  _GETORDERLISTRESPONSE._serialized_start=427
  _GETORDERLISTRESPONSE._serialized_end=471
  _ORDERSFUNCS._serialized_start=473
  _ORDERSFUNCS._serialized_end=596
# @@protoc_insertion_point(module_scope)
