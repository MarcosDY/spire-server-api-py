# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spire/api/agent/debug/v1/debug.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from spire.api.types import spiffeid_pb2 as spire_dot_api_dot_types_dot_spiffeid__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$spire/api/agent/debug/v1/debug.proto\x12\x14spire.agent.debug.v1\x1a\x1espire/api/types/spiffeid.proto\"\x10\n\x0eGetInfoRequest\"\xe5\x01\n\x0fGetInfoResponse\x12>\n\nsvid_chain\x18\x01 \x03(\x0b\x32*.spire.agent.debug.v1.GetInfoResponse.Cert\x12\x0e\n\x06uptime\x18\x02 \x01(\x05\x12\x13\n\x0bsvids_count\x18\x03 \x01(\x05\x12\x19\n\x11last_sync_success\x18\x04 \x01(\x03\x1aR\n\x04\x43\x65rt\x12%\n\x02id\x18\x01 \x01(\x0b\x32\x19.spire.api.types.SPIFFEID\x12\x12\n\nexpires_at\x18\x02 \x01(\x03\x12\x0f\n\x07subject\x18\x03 \x01(\t2_\n\x05\x44\x65\x62ug\x12V\n\x07GetInfo\x12$.spire.agent.debug.v1.GetInfoRequest\x1a%.spire.agent.debug.v1.GetInfoResponseBHZFgithub.com/spiffe/spire-api-sdk/proto/spire/api/agent/debug/v1;debugv1b\x06proto3')



_GETINFOREQUEST = DESCRIPTOR.message_types_by_name['GetInfoRequest']
_GETINFORESPONSE = DESCRIPTOR.message_types_by_name['GetInfoResponse']
_GETINFORESPONSE_CERT = _GETINFORESPONSE.nested_types_by_name['Cert']
GetInfoRequest = _reflection.GeneratedProtocolMessageType('GetInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETINFOREQUEST,
  '__module__' : 'spire.api.agent.debug.v1.debug_pb2'
  # @@protoc_insertion_point(class_scope:spire.agent.debug.v1.GetInfoRequest)
  })
_sym_db.RegisterMessage(GetInfoRequest)

GetInfoResponse = _reflection.GeneratedProtocolMessageType('GetInfoResponse', (_message.Message,), {

  'Cert' : _reflection.GeneratedProtocolMessageType('Cert', (_message.Message,), {
    'DESCRIPTOR' : _GETINFORESPONSE_CERT,
    '__module__' : 'spire.api.agent.debug.v1.debug_pb2'
    # @@protoc_insertion_point(class_scope:spire.agent.debug.v1.GetInfoResponse.Cert)
    })
  ,
  'DESCRIPTOR' : _GETINFORESPONSE,
  '__module__' : 'spire.api.agent.debug.v1.debug_pb2'
  # @@protoc_insertion_point(class_scope:spire.agent.debug.v1.GetInfoResponse)
  })
_sym_db.RegisterMessage(GetInfoResponse)
_sym_db.RegisterMessage(GetInfoResponse.Cert)

_DEBUG = DESCRIPTOR.services_by_name['Debug']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZFgithub.com/spiffe/spire-api-sdk/proto/spire/api/agent/debug/v1;debugv1'
  _GETINFOREQUEST._serialized_start=94
  _GETINFOREQUEST._serialized_end=110
  _GETINFORESPONSE._serialized_start=113
  _GETINFORESPONSE._serialized_end=342
  _GETINFORESPONSE_CERT._serialized_start=260
  _GETINFORESPONSE_CERT._serialized_end=342
  _DEBUG._serialized_start=344
  _DEBUG._serialized_end=439
# @@protoc_insertion_point(module_scope)