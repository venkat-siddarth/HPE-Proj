# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: products.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eproducts.proto\"\x8b\x01\n\x07product\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x18\n\x10get_absolute_url\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\r\n\x05price\x18\x05 \x01(\x01\x12\x11\n\tget_image\x18\x06 \x01(\t\x12\x15\n\rget_thumbnail\x18\x07 \x01(\t\"Z\n\x08\x63\x61tegory\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x18\n\x10get_absolute_url\x18\x03 \x01(\t\x12\x1a\n\x08products\x18\x04 \x03(\x0b\x32\x08.product\"\x17\n\x15latestProductsRequest\"3\n\x16latestProductsResponse\x12\x19\n\x07product\x18\x01 \x03(\x0b\x32\x08.product\"B\n\x15productDetailsRequest\x12\x14\n\x0c\x63\x61tegoryslug\x18\x01 \x01(\t\x12\x13\n\x0bproductslug\x18\x02 \x01(\t\"3\n\x16productDetailsResponse\x12\x19\n\x07product\x18\x01 \x01(\x0b\x32\x08.product\"/\n\x17\x43\x61tegoryProductsRequest\x12\x14\n\x0c\x63\x61tegoryslug\x18\x01 \x01(\t\"7\n\x18\x43\x61tegoryProductsResponse\x12\x1b\n\x08\x63\x61tegory\x18\x01 \x01(\x0b\x32\t.category\"\x1b\n\rprodIDRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"+\n\x0eprodIDResponse\x12\x19\n\x07product\x18\x01 \x01(\x0b\x32\x08.product\"\x1e\n\rsearchRequest\x12\r\n\x05query\x18\x01 \x01(\t\"+\n\x0esearchResponse\x12\x19\n\x07product\x18\x01 \x03(\x0b\x32\x08.product2\xb1\x02\n\x0cproductfuncs\x12\x41\n\x0egetproductlist\x12\x16.latestProductsRequest\x1a\x17.latestProductsResponse\x12\x44\n\x11getproductdetails\x12\x16.productDetailsRequest\x1a\x17.productDetailsResponse\x12)\n\x06search\x12\x0e.searchRequest\x1a\x0f.searchResponse\x12%\n\x02id\x12\x0e.prodIDRequest\x1a\x0f.prodIDResponse\x12\x46\n\x0fgetcategorylist\x12\x18.CategoryProductsRequest\x1a\x19.CategoryProductsResponseb\x06proto3')



_PRODUCT = DESCRIPTOR.message_types_by_name['product']
_CATEGORY = DESCRIPTOR.message_types_by_name['category']
_LATESTPRODUCTSREQUEST = DESCRIPTOR.message_types_by_name['latestProductsRequest']
_LATESTPRODUCTSRESPONSE = DESCRIPTOR.message_types_by_name['latestProductsResponse']
_PRODUCTDETAILSREQUEST = DESCRIPTOR.message_types_by_name['productDetailsRequest']
_PRODUCTDETAILSRESPONSE = DESCRIPTOR.message_types_by_name['productDetailsResponse']
_CATEGORYPRODUCTSREQUEST = DESCRIPTOR.message_types_by_name['CategoryProductsRequest']
_CATEGORYPRODUCTSRESPONSE = DESCRIPTOR.message_types_by_name['CategoryProductsResponse']
_PRODIDREQUEST = DESCRIPTOR.message_types_by_name['prodIDRequest']
_PRODIDRESPONSE = DESCRIPTOR.message_types_by_name['prodIDResponse']
_SEARCHREQUEST = DESCRIPTOR.message_types_by_name['searchRequest']
_SEARCHRESPONSE = DESCRIPTOR.message_types_by_name['searchResponse']
product = _reflection.GeneratedProtocolMessageType('product', (_message.Message,), {
  'DESCRIPTOR' : _PRODUCT,
  '__module__' : 'products_pb2'
  # @@protoc_insertion_point(class_scope:product)
  })
_sym_db.RegisterMessage(product)

category = _reflection.GeneratedProtocolMessageType('category', (_message.Message,), {
  'DESCRIPTOR' : _CATEGORY,
  '__module__' : 'products_pb2'
  # @@protoc_insertion_point(class_scope:category)
  })
_sym_db.RegisterMessage(category)

latestProductsRequest = _reflection.GeneratedProtocolMessageType('latestProductsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LATESTPRODUCTSREQUEST,
  '__module__' : 'products_pb2'
  # @@protoc_insertion_point(class_scope:latestProductsRequest)
  })
_sym_db.RegisterMessage(latestProductsRequest)

latestProductsResponse = _reflection.GeneratedProtocolMessageType('latestProductsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LATESTPRODUCTSRESPONSE,
  '__module__' : 'products_pb2'
  # @@protoc_insertion_point(class_scope:latestProductsResponse)
  })
_sym_db.RegisterMessage(latestProductsResponse)

productDetailsRequest = _reflection.GeneratedProtocolMessageType('productDetailsRequest', (_message.Message,), {
  'DESCRIPTOR' : _PRODUCTDETAILSREQUEST,
  '__module__' : 'products_pb2'
  # @@protoc_insertion_point(class_scope:productDetailsRequest)
  })
_sym_db.RegisterMessage(productDetailsRequest)

productDetailsResponse = _reflection.GeneratedProtocolMessageType('productDetailsResponse', (_message.Message,), {
  'DESCRIPTOR' : _PRODUCTDETAILSRESPONSE,
  '__module__' : 'products_pb2'
  # @@protoc_insertion_point(class_scope:productDetailsResponse)
  })
_sym_db.RegisterMessage(productDetailsResponse)

CategoryProductsRequest = _reflection.GeneratedProtocolMessageType('CategoryProductsRequest', (_message.Message,), {
  'DESCRIPTOR' : _CATEGORYPRODUCTSREQUEST,
  '__module__' : 'products_pb2'
  # @@protoc_insertion_point(class_scope:CategoryProductsRequest)
  })
_sym_db.RegisterMessage(CategoryProductsRequest)

CategoryProductsResponse = _reflection.GeneratedProtocolMessageType('CategoryProductsResponse', (_message.Message,), {
  'DESCRIPTOR' : _CATEGORYPRODUCTSRESPONSE,
  '__module__' : 'products_pb2'
  # @@protoc_insertion_point(class_scope:CategoryProductsResponse)
  })
_sym_db.RegisterMessage(CategoryProductsResponse)

prodIDRequest = _reflection.GeneratedProtocolMessageType('prodIDRequest', (_message.Message,), {
  'DESCRIPTOR' : _PRODIDREQUEST,
  '__module__' : 'products_pb2'
  # @@protoc_insertion_point(class_scope:prodIDRequest)
  })
_sym_db.RegisterMessage(prodIDRequest)

prodIDResponse = _reflection.GeneratedProtocolMessageType('prodIDResponse', (_message.Message,), {
  'DESCRIPTOR' : _PRODIDRESPONSE,
  '__module__' : 'products_pb2'
  # @@protoc_insertion_point(class_scope:prodIDResponse)
  })
_sym_db.RegisterMessage(prodIDResponse)

searchRequest = _reflection.GeneratedProtocolMessageType('searchRequest', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHREQUEST,
  '__module__' : 'products_pb2'
  # @@protoc_insertion_point(class_scope:searchRequest)
  })
_sym_db.RegisterMessage(searchRequest)

searchResponse = _reflection.GeneratedProtocolMessageType('searchResponse', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHRESPONSE,
  '__module__' : 'products_pb2'
  # @@protoc_insertion_point(class_scope:searchResponse)
  })
_sym_db.RegisterMessage(searchResponse)

_PRODUCTFUNCS = DESCRIPTOR.services_by_name['productfuncs']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PRODUCT._serialized_start=19
  _PRODUCT._serialized_end=158
  _CATEGORY._serialized_start=160
  _CATEGORY._serialized_end=250
  _LATESTPRODUCTSREQUEST._serialized_start=252
  _LATESTPRODUCTSREQUEST._serialized_end=275
  _LATESTPRODUCTSRESPONSE._serialized_start=277
  _LATESTPRODUCTSRESPONSE._serialized_end=328
  _PRODUCTDETAILSREQUEST._serialized_start=330
  _PRODUCTDETAILSREQUEST._serialized_end=396
  _PRODUCTDETAILSRESPONSE._serialized_start=398
  _PRODUCTDETAILSRESPONSE._serialized_end=449
  _CATEGORYPRODUCTSREQUEST._serialized_start=451
  _CATEGORYPRODUCTSREQUEST._serialized_end=498
  _CATEGORYPRODUCTSRESPONSE._serialized_start=500
  _CATEGORYPRODUCTSRESPONSE._serialized_end=555
  _PRODIDREQUEST._serialized_start=557
  _PRODIDREQUEST._serialized_end=584
  _PRODIDRESPONSE._serialized_start=586
  _PRODIDRESPONSE._serialized_end=629
  _SEARCHREQUEST._serialized_start=631
  _SEARCHREQUEST._serialized_end=661
  _SEARCHRESPONSE._serialized_start=663
  _SEARCHRESPONSE._serialized_end=706
  _PRODUCTFUNCS._serialized_start=709
  _PRODUCTFUNCS._serialized_end=1014
# @@protoc_insertion_point(module_scope)
