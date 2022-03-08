# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from spire.api.server.trustdomain.v1 import trustdomain_pb2 as spire_dot_api_dot_server_dot_trustdomain_dot_v1_dot_trustdomain__pb2
from spire.api.types import federationrelationship_pb2 as spire_dot_api_dot_types_dot_federationrelationship__pb2


class TrustDomainStub(object):
    """Manages the federation relationships with foreign trust domains.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListFederationRelationships = channel.unary_unary(
                '/spire.api.server.trustdomain.v1.TrustDomain/ListFederationRelationships',
                request_serializer=spire_dot_api_dot_server_dot_trustdomain_dot_v1_dot_trustdomain__pb2.ListFederationRelationshipsRequest.SerializeToString,
                response_deserializer=spire_dot_api_dot_server_dot_trustdomain_dot_v1_dot_trustdomain__pb2.ListFederationRelationshipsResponse.FromString,
                )
        self.GetFederationRelationship = channel.unary_unary(
                '/spire.api.server.trustdomain.v1.TrustDomain/GetFederationRelationship',
                request_serializer=spire_dot_api_dot_server_dot_trustdomain_dot_v1_dot_trustdomain__pb2.GetFederationRelationshipRequest.SerializeToString,
                response_deserializer=spire_dot_api_dot_types_dot_federationrelationship__pb2.FederationRelationship.FromString,
                )
        self.BatchCreateFederationRelationship = channel.unary_unary(
                '/spire.api.server.trustdomain.v1.TrustDomain/BatchCreateFederationRelationship',
                request_serializer=spire_dot_api_dot_server_dot_trustdomain_dot_v1_dot_trustdomain__pb2.BatchCreateFederationRelationshipRequest.SerializeToString,
                response_deserializer=spire_dot_api_dot_server_dot_trustdomain_dot_v1_dot_trustdomain__pb2.BatchCreateFederationRelationshipResponse.FromString,
                )
        self.BatchUpdateFederationRelationship = channel.unary_unary(
                '/spire.api.server.trustdomain.v1.TrustDomain/BatchUpdateFederationRelationship',
                request_serializer=spire_dot_api_dot_server_dot_trustdomain_dot_v1_dot_trustdomain__pb2.BatchUpdateFederationRelationshipRequest.SerializeToString,
                response_deserializer=spire_dot_api_dot_server_dot_trustdomain_dot_v1_dot_trustdomain__pb2.BatchUpdateFederationRelationshipResponse.FromString,
                )
        self.BatchDeleteFederationRelationship = channel.unary_unary(
                '/spire.api.server.trustdomain.v1.TrustDomain/BatchDeleteFederationRelationship',
                request_serializer=spire_dot_api_dot_server_dot_trustdomain_dot_v1_dot_trustdomain__pb2.BatchDeleteFederationRelationshipRequest.SerializeToString,
                response_deserializer=spire_dot_api_dot_server_dot_trustdomain_dot_v1_dot_trustdomain__pb2.BatchDeleteFederationRelationshipResponse.FromString,
                )
        self.RefreshBundle = channel.unary_unary(
                '/spire.api.server.trustdomain.v1.TrustDomain/RefreshBundle',
                request_serializer=spire_dot_api_dot_server_dot_trustdomain_dot_v1_dot_trustdomain__pb2.RefreshBundleRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class TrustDomainServicer(object):
    """Manages the federation relationships with foreign trust domains.
    """

    def ListFederationRelationships(self, request, context):
        """Lists federation relationships with foreign trust domains.

        The caller must be local or present an admin X509-SVID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFederationRelationship(self, request, context):
        """Gets a federation relationship with a foreign trust domain.
        If there is no federation relationship with the specified
        trust domain, NOT_FOUND is returned.

        The caller must be local or present an admin X509-SVID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BatchCreateFederationRelationship(self, request, context):
        """Batch creates one or more federation relationships with
        foreign trust domains.

        The caller must be local or present an admin X509-SVID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BatchUpdateFederationRelationship(self, request, context):
        """Batch updates one or more federation relationships with
        foreign trust domains.

        The caller must be local or present an admin X509-SVID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BatchDeleteFederationRelationship(self, request, context):
        """Batch deletes federation relationships with foreign trust domains.

        The caller must be local or present an admin X509-SVID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RefreshBundle(self, request, context):
        """Refreshes the bundle from the specified federated trust domain.
        If there is not a federation relationship configured with the
        specified trust domain, NOT_FOUND is returned.

        The caller must be local or present an admin X509-SVID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TrustDomainServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListFederationRelationships': grpc.unary_unary_rpc_method_handler(
                    servicer.ListFederationRelationships,
                    request_deserializer=spire_dot_api_dot_server_dot_trustdomain_dot_v1_dot_trustdomain__pb2.ListFederationRelationshipsRequest.FromString,
                    response_serializer=spire_dot_api_dot_server_dot_trustdomain_dot_v1_dot_trustdomain__pb2.ListFederationRelationshipsResponse.SerializeToString,
            ),
            'GetFederationRelationship': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFederationRelationship,
                    request_deserializer=spire_dot_api_dot_server_dot_trustdomain_dot_v1_dot_trustdomain__pb2.GetFederationRelationshipRequest.FromString,
                    response_serializer=spire_dot_api_dot_types_dot_federationrelationship__pb2.FederationRelationship.SerializeToString,
            ),
            'BatchCreateFederationRelationship': grpc.unary_unary_rpc_method_handler(
                    servicer.BatchCreateFederationRelationship,
                    request_deserializer=spire_dot_api_dot_server_dot_trustdomain_dot_v1_dot_trustdomain__pb2.BatchCreateFederationRelationshipRequest.FromString,
                    response_serializer=spire_dot_api_dot_server_dot_trustdomain_dot_v1_dot_trustdomain__pb2.BatchCreateFederationRelationshipResponse.SerializeToString,
            ),
            'BatchUpdateFederationRelationship': grpc.unary_unary_rpc_method_handler(
                    servicer.BatchUpdateFederationRelationship,
                    request_deserializer=spire_dot_api_dot_server_dot_trustdomain_dot_v1_dot_trustdomain__pb2.BatchUpdateFederationRelationshipRequest.FromString,
                    response_serializer=spire_dot_api_dot_server_dot_trustdomain_dot_v1_dot_trustdomain__pb2.BatchUpdateFederationRelationshipResponse.SerializeToString,
            ),
            'BatchDeleteFederationRelationship': grpc.unary_unary_rpc_method_handler(
                    servicer.BatchDeleteFederationRelationship,
                    request_deserializer=spire_dot_api_dot_server_dot_trustdomain_dot_v1_dot_trustdomain__pb2.BatchDeleteFederationRelationshipRequest.FromString,
                    response_serializer=spire_dot_api_dot_server_dot_trustdomain_dot_v1_dot_trustdomain__pb2.BatchDeleteFederationRelationshipResponse.SerializeToString,
            ),
            'RefreshBundle': grpc.unary_unary_rpc_method_handler(
                    servicer.RefreshBundle,
                    request_deserializer=spire_dot_api_dot_server_dot_trustdomain_dot_v1_dot_trustdomain__pb2.RefreshBundleRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'spire.api.server.trustdomain.v1.TrustDomain', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TrustDomain(object):
    """Manages the federation relationships with foreign trust domains.
    """

    @staticmethod
    def ListFederationRelationships(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spire.api.server.trustdomain.v1.TrustDomain/ListFederationRelationships',
            spire_dot_api_dot_server_dot_trustdomain_dot_v1_dot_trustdomain__pb2.ListFederationRelationshipsRequest.SerializeToString,
            spire_dot_api_dot_server_dot_trustdomain_dot_v1_dot_trustdomain__pb2.ListFederationRelationshipsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetFederationRelationship(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spire.api.server.trustdomain.v1.TrustDomain/GetFederationRelationship',
            spire_dot_api_dot_server_dot_trustdomain_dot_v1_dot_trustdomain__pb2.GetFederationRelationshipRequest.SerializeToString,
            spire_dot_api_dot_types_dot_federationrelationship__pb2.FederationRelationship.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BatchCreateFederationRelationship(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spire.api.server.trustdomain.v1.TrustDomain/BatchCreateFederationRelationship',
            spire_dot_api_dot_server_dot_trustdomain_dot_v1_dot_trustdomain__pb2.BatchCreateFederationRelationshipRequest.SerializeToString,
            spire_dot_api_dot_server_dot_trustdomain_dot_v1_dot_trustdomain__pb2.BatchCreateFederationRelationshipResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BatchUpdateFederationRelationship(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spire.api.server.trustdomain.v1.TrustDomain/BatchUpdateFederationRelationship',
            spire_dot_api_dot_server_dot_trustdomain_dot_v1_dot_trustdomain__pb2.BatchUpdateFederationRelationshipRequest.SerializeToString,
            spire_dot_api_dot_server_dot_trustdomain_dot_v1_dot_trustdomain__pb2.BatchUpdateFederationRelationshipResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BatchDeleteFederationRelationship(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spire.api.server.trustdomain.v1.TrustDomain/BatchDeleteFederationRelationship',
            spire_dot_api_dot_server_dot_trustdomain_dot_v1_dot_trustdomain__pb2.BatchDeleteFederationRelationshipRequest.SerializeToString,
            spire_dot_api_dot_server_dot_trustdomain_dot_v1_dot_trustdomain__pb2.BatchDeleteFederationRelationshipResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RefreshBundle(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spire.api.server.trustdomain.v1.TrustDomain/RefreshBundle',
            spire_dot_api_dot_server_dot_trustdomain_dot_v1_dot_trustdomain__pb2.RefreshBundleRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
