# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spire/api/server/trustdomain/v1/trustdomain.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from spire.api.types import federationrelationship_pb2 as spire_dot_api_dot_types_dot_federationrelationship__pb2
from spire.api.types import status_pb2 as spire_dot_api_dot_types_dot_status__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1spire/api/server/trustdomain/v1/trustdomain.proto\x12\x1fspire.api.server.trustdomain.v1\x1a\x1bgoogle/protobuf/empty.proto\x1a,spire/api/types/federationrelationship.proto\x1a\x1cspire/api/types/status.proto\"\x8d\x01\n\"ListFederationRelationshipsRequest\x12@\n\x0boutput_mask\x18\x01 \x01(\x0b\x32+.spire.api.types.FederationRelationshipMask\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\"\x89\x01\n#ListFederationRelationshipsResponse\x12I\n\x18\x66\x65\x64\x65ration_relationships\x18\x01 \x03(\x0b\x32\'.spire.api.types.FederationRelationship\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"z\n GetFederationRelationshipRequest\x12\x14\n\x0ctrust_domain\x18\x01 \x01(\t\x12@\n\x0boutput_mask\x18\x02 \x01(\x0b\x32+.spire.api.types.FederationRelationshipMask\"\xb7\x01\n(BatchCreateFederationRelationshipRequest\x12I\n\x18\x66\x65\x64\x65ration_relationships\x18\x01 \x03(\x0b\x32\'.spire.api.types.FederationRelationship\x12@\n\x0boutput_mask\x18\x02 \x01(\x0b\x32+.spire.api.types.FederationRelationshipMask\"\x8c\x02\n)BatchCreateFederationRelationshipResponse\x12\x62\n\x07results\x18\x01 \x03(\x0b\x32Q.spire.api.server.trustdomain.v1.BatchCreateFederationRelationshipResponse.Result\x1a{\n\x06Result\x12\'\n\x06status\x18\x01 \x01(\x0b\x32\x17.spire.api.types.Status\x12H\n\x17\x66\x65\x64\x65ration_relationship\x18\x02 \x01(\x0b\x32\'.spire.api.types.FederationRelationship\"\xf8\x01\n(BatchUpdateFederationRelationshipRequest\x12I\n\x18\x66\x65\x64\x65ration_relationships\x18\x01 \x03(\x0b\x32\'.spire.api.types.FederationRelationship\x12?\n\ninput_mask\x18\x02 \x01(\x0b\x32+.spire.api.types.FederationRelationshipMask\x12@\n\x0boutput_mask\x18\x03 \x01(\x0b\x32+.spire.api.types.FederationRelationshipMask\"\x8c\x02\n)BatchUpdateFederationRelationshipResponse\x12\x62\n\x07results\x18\x01 \x03(\x0b\x32Q.spire.api.server.trustdomain.v1.BatchUpdateFederationRelationshipResponse.Result\x1a{\n\x06Result\x12\'\n\x06status\x18\x01 \x01(\x0b\x32\x17.spire.api.types.Status\x12H\n\x17\x66\x65\x64\x65ration_relationship\x18\x02 \x01(\x0b\x32\'.spire.api.types.FederationRelationship\"A\n(BatchDeleteFederationRelationshipRequest\x12\x15\n\rtrust_domains\x18\x01 \x03(\t\"\xd8\x01\n)BatchDeleteFederationRelationshipResponse\x12\x62\n\x07results\x18\x01 \x03(\x0b\x32Q.spire.api.server.trustdomain.v1.BatchDeleteFederationRelationshipResponse.Result\x1aG\n\x06Result\x12\'\n\x06status\x18\x01 \x01(\x0b\x32\x17.spire.api.types.Status\x12\x14\n\x0ctrust_domain\x18\x02 \x01(\t\",\n\x14RefreshBundleRequest\x12\x14\n\x0ctrust_domain\x18\x01 \x01(\t2\xd9\x07\n\x0bTrustDomain\x12\xa8\x01\n\x1bListFederationRelationships\x12\x43.spire.api.server.trustdomain.v1.ListFederationRelationshipsRequest\x1a\x44.spire.api.server.trustdomain.v1.ListFederationRelationshipsResponse\x12\x87\x01\n\x19GetFederationRelationship\x12\x41.spire.api.server.trustdomain.v1.GetFederationRelationshipRequest\x1a\'.spire.api.types.FederationRelationship\x12\xba\x01\n!BatchCreateFederationRelationship\x12I.spire.api.server.trustdomain.v1.BatchCreateFederationRelationshipRequest\x1aJ.spire.api.server.trustdomain.v1.BatchCreateFederationRelationshipResponse\x12\xba\x01\n!BatchUpdateFederationRelationship\x12I.spire.api.server.trustdomain.v1.BatchUpdateFederationRelationshipRequest\x1aJ.spire.api.server.trustdomain.v1.BatchUpdateFederationRelationshipResponse\x12\xba\x01\n!BatchDeleteFederationRelationship\x12I.spire.api.server.trustdomain.v1.BatchDeleteFederationRelationshipRequest\x1aJ.spire.api.server.trustdomain.v1.BatchDeleteFederationRelationshipResponse\x12^\n\rRefreshBundle\x12\x35.spire.api.server.trustdomain.v1.RefreshBundleRequest\x1a\x16.google.protobuf.EmptyBSZQgithub.com/spiffe/spire-api-sdk/proto/spire/api/server/trustdomain/v1;trustdomainb\x06proto3')



_LISTFEDERATIONRELATIONSHIPSREQUEST = DESCRIPTOR.message_types_by_name['ListFederationRelationshipsRequest']
_LISTFEDERATIONRELATIONSHIPSRESPONSE = DESCRIPTOR.message_types_by_name['ListFederationRelationshipsResponse']
_GETFEDERATIONRELATIONSHIPREQUEST = DESCRIPTOR.message_types_by_name['GetFederationRelationshipRequest']
_BATCHCREATEFEDERATIONRELATIONSHIPREQUEST = DESCRIPTOR.message_types_by_name['BatchCreateFederationRelationshipRequest']
_BATCHCREATEFEDERATIONRELATIONSHIPRESPONSE = DESCRIPTOR.message_types_by_name['BatchCreateFederationRelationshipResponse']
_BATCHCREATEFEDERATIONRELATIONSHIPRESPONSE_RESULT = _BATCHCREATEFEDERATIONRELATIONSHIPRESPONSE.nested_types_by_name['Result']
_BATCHUPDATEFEDERATIONRELATIONSHIPREQUEST = DESCRIPTOR.message_types_by_name['BatchUpdateFederationRelationshipRequest']
_BATCHUPDATEFEDERATIONRELATIONSHIPRESPONSE = DESCRIPTOR.message_types_by_name['BatchUpdateFederationRelationshipResponse']
_BATCHUPDATEFEDERATIONRELATIONSHIPRESPONSE_RESULT = _BATCHUPDATEFEDERATIONRELATIONSHIPRESPONSE.nested_types_by_name['Result']
_BATCHDELETEFEDERATIONRELATIONSHIPREQUEST = DESCRIPTOR.message_types_by_name['BatchDeleteFederationRelationshipRequest']
_BATCHDELETEFEDERATIONRELATIONSHIPRESPONSE = DESCRIPTOR.message_types_by_name['BatchDeleteFederationRelationshipResponse']
_BATCHDELETEFEDERATIONRELATIONSHIPRESPONSE_RESULT = _BATCHDELETEFEDERATIONRELATIONSHIPRESPONSE.nested_types_by_name['Result']
_REFRESHBUNDLEREQUEST = DESCRIPTOR.message_types_by_name['RefreshBundleRequest']
ListFederationRelationshipsRequest = _reflection.GeneratedProtocolMessageType('ListFederationRelationshipsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTFEDERATIONRELATIONSHIPSREQUEST,
  '__module__' : 'spire.api.server.trustdomain.v1.trustdomain_pb2'
  # @@protoc_insertion_point(class_scope:spire.api.server.trustdomain.v1.ListFederationRelationshipsRequest)
  })
_sym_db.RegisterMessage(ListFederationRelationshipsRequest)

ListFederationRelationshipsResponse = _reflection.GeneratedProtocolMessageType('ListFederationRelationshipsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTFEDERATIONRELATIONSHIPSRESPONSE,
  '__module__' : 'spire.api.server.trustdomain.v1.trustdomain_pb2'
  # @@protoc_insertion_point(class_scope:spire.api.server.trustdomain.v1.ListFederationRelationshipsResponse)
  })
_sym_db.RegisterMessage(ListFederationRelationshipsResponse)

GetFederationRelationshipRequest = _reflection.GeneratedProtocolMessageType('GetFederationRelationshipRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETFEDERATIONRELATIONSHIPREQUEST,
  '__module__' : 'spire.api.server.trustdomain.v1.trustdomain_pb2'
  # @@protoc_insertion_point(class_scope:spire.api.server.trustdomain.v1.GetFederationRelationshipRequest)
  })
_sym_db.RegisterMessage(GetFederationRelationshipRequest)

BatchCreateFederationRelationshipRequest = _reflection.GeneratedProtocolMessageType('BatchCreateFederationRelationshipRequest', (_message.Message,), {
  'DESCRIPTOR' : _BATCHCREATEFEDERATIONRELATIONSHIPREQUEST,
  '__module__' : 'spire.api.server.trustdomain.v1.trustdomain_pb2'
  # @@protoc_insertion_point(class_scope:spire.api.server.trustdomain.v1.BatchCreateFederationRelationshipRequest)
  })
_sym_db.RegisterMessage(BatchCreateFederationRelationshipRequest)

BatchCreateFederationRelationshipResponse = _reflection.GeneratedProtocolMessageType('BatchCreateFederationRelationshipResponse', (_message.Message,), {

  'Result' : _reflection.GeneratedProtocolMessageType('Result', (_message.Message,), {
    'DESCRIPTOR' : _BATCHCREATEFEDERATIONRELATIONSHIPRESPONSE_RESULT,
    '__module__' : 'spire.api.server.trustdomain.v1.trustdomain_pb2'
    # @@protoc_insertion_point(class_scope:spire.api.server.trustdomain.v1.BatchCreateFederationRelationshipResponse.Result)
    })
  ,
  'DESCRIPTOR' : _BATCHCREATEFEDERATIONRELATIONSHIPRESPONSE,
  '__module__' : 'spire.api.server.trustdomain.v1.trustdomain_pb2'
  # @@protoc_insertion_point(class_scope:spire.api.server.trustdomain.v1.BatchCreateFederationRelationshipResponse)
  })
_sym_db.RegisterMessage(BatchCreateFederationRelationshipResponse)
_sym_db.RegisterMessage(BatchCreateFederationRelationshipResponse.Result)

BatchUpdateFederationRelationshipRequest = _reflection.GeneratedProtocolMessageType('BatchUpdateFederationRelationshipRequest', (_message.Message,), {
  'DESCRIPTOR' : _BATCHUPDATEFEDERATIONRELATIONSHIPREQUEST,
  '__module__' : 'spire.api.server.trustdomain.v1.trustdomain_pb2'
  # @@protoc_insertion_point(class_scope:spire.api.server.trustdomain.v1.BatchUpdateFederationRelationshipRequest)
  })
_sym_db.RegisterMessage(BatchUpdateFederationRelationshipRequest)

BatchUpdateFederationRelationshipResponse = _reflection.GeneratedProtocolMessageType('BatchUpdateFederationRelationshipResponse', (_message.Message,), {

  'Result' : _reflection.GeneratedProtocolMessageType('Result', (_message.Message,), {
    'DESCRIPTOR' : _BATCHUPDATEFEDERATIONRELATIONSHIPRESPONSE_RESULT,
    '__module__' : 'spire.api.server.trustdomain.v1.trustdomain_pb2'
    # @@protoc_insertion_point(class_scope:spire.api.server.trustdomain.v1.BatchUpdateFederationRelationshipResponse.Result)
    })
  ,
  'DESCRIPTOR' : _BATCHUPDATEFEDERATIONRELATIONSHIPRESPONSE,
  '__module__' : 'spire.api.server.trustdomain.v1.trustdomain_pb2'
  # @@protoc_insertion_point(class_scope:spire.api.server.trustdomain.v1.BatchUpdateFederationRelationshipResponse)
  })
_sym_db.RegisterMessage(BatchUpdateFederationRelationshipResponse)
_sym_db.RegisterMessage(BatchUpdateFederationRelationshipResponse.Result)

BatchDeleteFederationRelationshipRequest = _reflection.GeneratedProtocolMessageType('BatchDeleteFederationRelationshipRequest', (_message.Message,), {
  'DESCRIPTOR' : _BATCHDELETEFEDERATIONRELATIONSHIPREQUEST,
  '__module__' : 'spire.api.server.trustdomain.v1.trustdomain_pb2'
  # @@protoc_insertion_point(class_scope:spire.api.server.trustdomain.v1.BatchDeleteFederationRelationshipRequest)
  })
_sym_db.RegisterMessage(BatchDeleteFederationRelationshipRequest)

BatchDeleteFederationRelationshipResponse = _reflection.GeneratedProtocolMessageType('BatchDeleteFederationRelationshipResponse', (_message.Message,), {

  'Result' : _reflection.GeneratedProtocolMessageType('Result', (_message.Message,), {
    'DESCRIPTOR' : _BATCHDELETEFEDERATIONRELATIONSHIPRESPONSE_RESULT,
    '__module__' : 'spire.api.server.trustdomain.v1.trustdomain_pb2'
    # @@protoc_insertion_point(class_scope:spire.api.server.trustdomain.v1.BatchDeleteFederationRelationshipResponse.Result)
    })
  ,
  'DESCRIPTOR' : _BATCHDELETEFEDERATIONRELATIONSHIPRESPONSE,
  '__module__' : 'spire.api.server.trustdomain.v1.trustdomain_pb2'
  # @@protoc_insertion_point(class_scope:spire.api.server.trustdomain.v1.BatchDeleteFederationRelationshipResponse)
  })
_sym_db.RegisterMessage(BatchDeleteFederationRelationshipResponse)
_sym_db.RegisterMessage(BatchDeleteFederationRelationshipResponse.Result)

RefreshBundleRequest = _reflection.GeneratedProtocolMessageType('RefreshBundleRequest', (_message.Message,), {
  'DESCRIPTOR' : _REFRESHBUNDLEREQUEST,
  '__module__' : 'spire.api.server.trustdomain.v1.trustdomain_pb2'
  # @@protoc_insertion_point(class_scope:spire.api.server.trustdomain.v1.RefreshBundleRequest)
  })
_sym_db.RegisterMessage(RefreshBundleRequest)

_TRUSTDOMAIN = DESCRIPTOR.services_by_name['TrustDomain']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZQgithub.com/spiffe/spire-api-sdk/proto/spire/api/server/trustdomain/v1;trustdomain'
  _LISTFEDERATIONRELATIONSHIPSREQUEST._serialized_start=192
  _LISTFEDERATIONRELATIONSHIPSREQUEST._serialized_end=333
  _LISTFEDERATIONRELATIONSHIPSRESPONSE._serialized_start=336
  _LISTFEDERATIONRELATIONSHIPSRESPONSE._serialized_end=473
  _GETFEDERATIONRELATIONSHIPREQUEST._serialized_start=475
  _GETFEDERATIONRELATIONSHIPREQUEST._serialized_end=597
  _BATCHCREATEFEDERATIONRELATIONSHIPREQUEST._serialized_start=600
  _BATCHCREATEFEDERATIONRELATIONSHIPREQUEST._serialized_end=783
  _BATCHCREATEFEDERATIONRELATIONSHIPRESPONSE._serialized_start=786
  _BATCHCREATEFEDERATIONRELATIONSHIPRESPONSE._serialized_end=1054
  _BATCHCREATEFEDERATIONRELATIONSHIPRESPONSE_RESULT._serialized_start=931
  _BATCHCREATEFEDERATIONRELATIONSHIPRESPONSE_RESULT._serialized_end=1054
  _BATCHUPDATEFEDERATIONRELATIONSHIPREQUEST._serialized_start=1057
  _BATCHUPDATEFEDERATIONRELATIONSHIPREQUEST._serialized_end=1305
  _BATCHUPDATEFEDERATIONRELATIONSHIPRESPONSE._serialized_start=1308
  _BATCHUPDATEFEDERATIONRELATIONSHIPRESPONSE._serialized_end=1576
  _BATCHUPDATEFEDERATIONRELATIONSHIPRESPONSE_RESULT._serialized_start=931
  _BATCHUPDATEFEDERATIONRELATIONSHIPRESPONSE_RESULT._serialized_end=1054
  _BATCHDELETEFEDERATIONRELATIONSHIPREQUEST._serialized_start=1578
  _BATCHDELETEFEDERATIONRELATIONSHIPREQUEST._serialized_end=1643
  _BATCHDELETEFEDERATIONRELATIONSHIPRESPONSE._serialized_start=1646
  _BATCHDELETEFEDERATIONRELATIONSHIPRESPONSE._serialized_end=1862
  _BATCHDELETEFEDERATIONRELATIONSHIPRESPONSE_RESULT._serialized_start=1791
  _BATCHDELETEFEDERATIONRELATIONSHIPRESPONSE_RESULT._serialized_end=1862
  _REFRESHBUNDLEREQUEST._serialized_start=1864
  _REFRESHBUNDLEREQUEST._serialized_end=1908
  _TRUSTDOMAIN._serialized_start=1911
  _TRUSTDOMAIN._serialized_end=2896
# @@protoc_insertion_point(module_scope)