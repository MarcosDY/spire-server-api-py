# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spire/api/server/debug/v1/debug.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from spire.api.types import spiffeid_pb2 as spire_dot_api_dot_types_dot_spiffeid__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%spire/api/server/debug/v1/debug.proto\x12\x19spire.api.server.debug.v1\x1a\x1espire/api/types/spiffeid.proto\"\x10\n\x0eGetInfoRequest\"\x88\x02\n\x0fGetInfoResponse\x12\x43\n\nsvid_chain\x18\x01 \x03(\x0b\x32/.spire.api.server.debug.v1.GetInfoResponse.Cert\x12\x0e\n\x06uptime\x18\x02 \x01(\x05\x12\x14\n\x0c\x61gents_count\x18\x03 \x01(\x05\x12\x1f\n\x17\x66\x65\x64\x65rated_bundles_count\x18\x04 \x01(\x05\x12\x15\n\rentries_count\x18\x05 \x01(\x05\x1aR\n\x04\x43\x65rt\x12%\n\x02id\x18\x01 \x01(\x0b\x32\x19.spire.api.types.SPIFFEID\x12\x12\n\nexpires_at\x18\x02 \x01(\x03\x12\x0f\n\x07subject\x18\x03 \x01(\t2i\n\x05\x44\x65\x62ug\x12`\n\x07GetInfo\x12).spire.api.server.debug.v1.GetInfoRequest\x1a*.spire.api.server.debug.v1.GetInfoResponseBIZGgithub.com/spiffe/spire-api-sdk/proto/spire/api/server/debug/v1;debugv1b\x06proto3')



_GETINFOREQUEST = DESCRIPTOR.message_types_by_name['GetInfoRequest']
_GETINFORESPONSE = DESCRIPTOR.message_types_by_name['GetInfoResponse']
_GETINFORESPONSE_CERT = _GETINFORESPONSE.nested_types_by_name['Cert']
GetInfoRequest = _reflection.GeneratedProtocolMessageType('GetInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETINFOREQUEST,
  '__module__' : 'spire.api.server.debug.v1.debug_pb2'
  # @@protoc_insertion_point(class_scope:spire.api.server.debug.v1.GetInfoRequest)
  })
_sym_db.RegisterMessage(GetInfoRequest)

GetInfoResponse = _reflection.GeneratedProtocolMessageType('GetInfoResponse', (_message.Message,), {

  'Cert' : _reflection.GeneratedProtocolMessageType('Cert', (_message.Message,), {
    'DESCRIPTOR' : _GETINFORESPONSE_CERT,
    '__module__' : 'spire.api.server.debug.v1.debug_pb2'
    # @@protoc_insertion_point(class_scope:spire.api.server.debug.v1.GetInfoResponse.Cert)
    })
  ,
  'DESCRIPTOR' : _GETINFORESPONSE,
  '__module__' : 'spire.api.server.debug.v1.debug_pb2'
  # @@protoc_insertion_point(class_scope:spire.api.server.debug.v1.GetInfoResponse)
  })
_sym_db.RegisterMessage(GetInfoResponse)
_sym_db.RegisterMessage(GetInfoResponse.Cert)

_DEBUG = DESCRIPTOR.services_by_name['Debug']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZGgithub.com/spiffe/spire-api-sdk/proto/spire/api/server/debug/v1;debugv1'
  _GETINFOREQUEST._serialized_start=100
  _GETINFOREQUEST._serialized_end=116
  _GETINFORESPONSE._serialized_start=119
  _GETINFORESPONSE._serialized_end=383
  _GETINFORESPONSE_CERT._serialized_start=301
  _GETINFORESPONSE_CERT._serialized_end=383
  _DEBUG._serialized_start=385
  _DEBUG._serialized_end=490
# @@protoc_insertion_point(module_scope)
