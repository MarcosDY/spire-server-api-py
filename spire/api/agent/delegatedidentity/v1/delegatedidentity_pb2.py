# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spire/api/agent/delegatedidentity/v1/delegatedidentity.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from spire.api.types import selector_pb2 as spire_dot_api_dot_types_dot_selector__pb2
from spire.api.types import x509svid_pb2 as spire_dot_api_dot_types_dot_x509svid__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<spire/api/agent/delegatedidentity/v1/delegatedidentity.proto\x12$spire.api.agent.delegatedidentity.v1\x1a\x1espire/api/types/selector.proto\x1a\x1espire/api/types/x509svid.proto\"V\n\x0fX509SVIDWithKey\x12,\n\tx509_svid\x18\x01 \x01(\x0b\x32\x19.spire.api.types.X509SVID\x12\x15\n\rx509_svid_key\x18\x02 \x01(\x0c\"K\n\x1bSubscribeToX509SVIDsRequest\x12,\n\tselectors\x18\x01 \x03(\x0b\x32\x19.spire.api.types.Selector\"\x81\x01\n\x1cSubscribeToX509SVIDsResponse\x12I\n\nx509_svids\x18\x01 \x03(\x0b\x32\x35.spire.api.agent.delegatedidentity.v1.X509SVIDWithKey\x12\x16\n\x0e\x66\x65\x64\x65rates_with\x18\x02 \x03(\t\"\x1f\n\x1dSubscribeToX509BundlesRequest\"\xca\x01\n\x1eSubscribeToX509BundlesResponse\x12q\n\x0f\x63\x61_certificates\x18\x01 \x03(\x0b\x32X.spire.api.agent.delegatedidentity.v1.SubscribeToX509BundlesResponse.CaCertificatesEntry\x1a\x35\n\x13\x43\x61\x43\x65rtificatesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\x32\xdd\x02\n\x11\x44\x65legatedIdentity\x12\x9f\x01\n\x14SubscribeToX509SVIDs\x12\x41.spire.api.agent.delegatedidentity.v1.SubscribeToX509SVIDsRequest\x1a\x42.spire.api.agent.delegatedidentity.v1.SubscribeToX509SVIDsResponse0\x01\x12\xa5\x01\n\x16SubscribeToX509Bundles\x12\x43.spire.api.agent.delegatedidentity.v1.SubscribeToX509BundlesRequest\x1a\x44.spire.api.agent.delegatedidentity.v1.SubscribeToX509BundlesResponse0\x01\x42`Z^github.com/spiffe/spire-api-sdk/proto/spire/api/agent/delegatedidentity/v1;delegatedidentityv1b\x06proto3')



_X509SVIDWITHKEY = DESCRIPTOR.message_types_by_name['X509SVIDWithKey']
_SUBSCRIBETOX509SVIDSREQUEST = DESCRIPTOR.message_types_by_name['SubscribeToX509SVIDsRequest']
_SUBSCRIBETOX509SVIDSRESPONSE = DESCRIPTOR.message_types_by_name['SubscribeToX509SVIDsResponse']
_SUBSCRIBETOX509BUNDLESREQUEST = DESCRIPTOR.message_types_by_name['SubscribeToX509BundlesRequest']
_SUBSCRIBETOX509BUNDLESRESPONSE = DESCRIPTOR.message_types_by_name['SubscribeToX509BundlesResponse']
_SUBSCRIBETOX509BUNDLESRESPONSE_CACERTIFICATESENTRY = _SUBSCRIBETOX509BUNDLESRESPONSE.nested_types_by_name['CaCertificatesEntry']
X509SVIDWithKey = _reflection.GeneratedProtocolMessageType('X509SVIDWithKey', (_message.Message,), {
  'DESCRIPTOR' : _X509SVIDWITHKEY,
  '__module__' : 'spire.api.agent.delegatedidentity.v1.delegatedidentity_pb2'
  # @@protoc_insertion_point(class_scope:spire.api.agent.delegatedidentity.v1.X509SVIDWithKey)
  })
_sym_db.RegisterMessage(X509SVIDWithKey)

SubscribeToX509SVIDsRequest = _reflection.GeneratedProtocolMessageType('SubscribeToX509SVIDsRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBETOX509SVIDSREQUEST,
  '__module__' : 'spire.api.agent.delegatedidentity.v1.delegatedidentity_pb2'
  # @@protoc_insertion_point(class_scope:spire.api.agent.delegatedidentity.v1.SubscribeToX509SVIDsRequest)
  })
_sym_db.RegisterMessage(SubscribeToX509SVIDsRequest)

SubscribeToX509SVIDsResponse = _reflection.GeneratedProtocolMessageType('SubscribeToX509SVIDsResponse', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBETOX509SVIDSRESPONSE,
  '__module__' : 'spire.api.agent.delegatedidentity.v1.delegatedidentity_pb2'
  # @@protoc_insertion_point(class_scope:spire.api.agent.delegatedidentity.v1.SubscribeToX509SVIDsResponse)
  })
_sym_db.RegisterMessage(SubscribeToX509SVIDsResponse)

SubscribeToX509BundlesRequest = _reflection.GeneratedProtocolMessageType('SubscribeToX509BundlesRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBETOX509BUNDLESREQUEST,
  '__module__' : 'spire.api.agent.delegatedidentity.v1.delegatedidentity_pb2'
  # @@protoc_insertion_point(class_scope:spire.api.agent.delegatedidentity.v1.SubscribeToX509BundlesRequest)
  })
_sym_db.RegisterMessage(SubscribeToX509BundlesRequest)

SubscribeToX509BundlesResponse = _reflection.GeneratedProtocolMessageType('SubscribeToX509BundlesResponse', (_message.Message,), {

  'CaCertificatesEntry' : _reflection.GeneratedProtocolMessageType('CaCertificatesEntry', (_message.Message,), {
    'DESCRIPTOR' : _SUBSCRIBETOX509BUNDLESRESPONSE_CACERTIFICATESENTRY,
    '__module__' : 'spire.api.agent.delegatedidentity.v1.delegatedidentity_pb2'
    # @@protoc_insertion_point(class_scope:spire.api.agent.delegatedidentity.v1.SubscribeToX509BundlesResponse.CaCertificatesEntry)
    })
  ,
  'DESCRIPTOR' : _SUBSCRIBETOX509BUNDLESRESPONSE,
  '__module__' : 'spire.api.agent.delegatedidentity.v1.delegatedidentity_pb2'
  # @@protoc_insertion_point(class_scope:spire.api.agent.delegatedidentity.v1.SubscribeToX509BundlesResponse)
  })
_sym_db.RegisterMessage(SubscribeToX509BundlesResponse)
_sym_db.RegisterMessage(SubscribeToX509BundlesResponse.CaCertificatesEntry)

_DELEGATEDIDENTITY = DESCRIPTOR.services_by_name['DelegatedIdentity']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z^github.com/spiffe/spire-api-sdk/proto/spire/api/agent/delegatedidentity/v1;delegatedidentityv1'
  _SUBSCRIBETOX509BUNDLESRESPONSE_CACERTIFICATESENTRY._options = None
  _SUBSCRIBETOX509BUNDLESRESPONSE_CACERTIFICATESENTRY._serialized_options = b'8\001'
  _X509SVIDWITHKEY._serialized_start=166
  _X509SVIDWITHKEY._serialized_end=252
  _SUBSCRIBETOX509SVIDSREQUEST._serialized_start=254
  _SUBSCRIBETOX509SVIDSREQUEST._serialized_end=329
  _SUBSCRIBETOX509SVIDSRESPONSE._serialized_start=332
  _SUBSCRIBETOX509SVIDSRESPONSE._serialized_end=461
  _SUBSCRIBETOX509BUNDLESREQUEST._serialized_start=463
  _SUBSCRIBETOX509BUNDLESREQUEST._serialized_end=494
  _SUBSCRIBETOX509BUNDLESRESPONSE._serialized_start=497
  _SUBSCRIBETOX509BUNDLESRESPONSE._serialized_end=699
  _SUBSCRIBETOX509BUNDLESRESPONSE_CACERTIFICATESENTRY._serialized_start=646
  _SUBSCRIBETOX509BUNDLESRESPONSE_CACERTIFICATESENTRY._serialized_end=699
  _DELEGATEDIDENTITY._serialized_start=702
  _DELEGATEDIDENTITY._serialized_end=1051
# @@protoc_insertion_point(module_scope)
