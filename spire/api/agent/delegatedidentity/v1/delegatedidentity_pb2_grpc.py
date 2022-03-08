# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from spire.api.agent.delegatedidentity.v1 import delegatedidentity_pb2 as spire_dot_api_dot_agent_dot_delegatedidentity_dot_v1_dot_delegatedidentity__pb2


class DelegatedIdentityStub(object):
    """The delegatedIdentity service provides an interface to get the SVIDs of other
    workloads on the host. This service is intended for use cases where a process
    (different than the workload one) should access the workload's SVID to
    perform actions on behalf of the workload. One example of is using a single
    node instance of Envoy that upgrades TCP connections for different processes
    running in such a node.

    The caller must be local and its identity must be listed in the allowed
    clients on the spire-agent configuration.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SubscribeToX509SVIDs = channel.unary_stream(
                '/spire.api.agent.delegatedidentity.v1.DelegatedIdentity/SubscribeToX509SVIDs',
                request_serializer=spire_dot_api_dot_agent_dot_delegatedidentity_dot_v1_dot_delegatedidentity__pb2.SubscribeToX509SVIDsRequest.SerializeToString,
                response_deserializer=spire_dot_api_dot_agent_dot_delegatedidentity_dot_v1_dot_delegatedidentity__pb2.SubscribeToX509SVIDsResponse.FromString,
                )
        self.SubscribeToX509Bundles = channel.unary_stream(
                '/spire.api.agent.delegatedidentity.v1.DelegatedIdentity/SubscribeToX509Bundles',
                request_serializer=spire_dot_api_dot_agent_dot_delegatedidentity_dot_v1_dot_delegatedidentity__pb2.SubscribeToX509BundlesRequest.SerializeToString,
                response_deserializer=spire_dot_api_dot_agent_dot_delegatedidentity_dot_v1_dot_delegatedidentity__pb2.SubscribeToX509BundlesResponse.FromString,
                )


class DelegatedIdentityServicer(object):
    """The delegatedIdentity service provides an interface to get the SVIDs of other
    workloads on the host. This service is intended for use cases where a process
    (different than the workload one) should access the workload's SVID to
    perform actions on behalf of the workload. One example of is using a single
    node instance of Envoy that upgrades TCP connections for different processes
    running in such a node.

    The caller must be local and its identity must be listed in the allowed
    clients on the spire-agent configuration.
    """

    def SubscribeToX509SVIDs(self, request, context):
        """Subscribe to get X.509-SVIDs for workloads that match the given selectors.
        The lifetime of the subscription aligns to the lifetime of the stream.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeToX509Bundles(self, request, context):
        """Subscribe to get local and all federated bundles.
        The lifetime of the subscription aligns to the lifetime of the stream.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DelegatedIdentityServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SubscribeToX509SVIDs': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeToX509SVIDs,
                    request_deserializer=spire_dot_api_dot_agent_dot_delegatedidentity_dot_v1_dot_delegatedidentity__pb2.SubscribeToX509SVIDsRequest.FromString,
                    response_serializer=spire_dot_api_dot_agent_dot_delegatedidentity_dot_v1_dot_delegatedidentity__pb2.SubscribeToX509SVIDsResponse.SerializeToString,
            ),
            'SubscribeToX509Bundles': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeToX509Bundles,
                    request_deserializer=spire_dot_api_dot_agent_dot_delegatedidentity_dot_v1_dot_delegatedidentity__pb2.SubscribeToX509BundlesRequest.FromString,
                    response_serializer=spire_dot_api_dot_agent_dot_delegatedidentity_dot_v1_dot_delegatedidentity__pb2.SubscribeToX509BundlesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'spire.api.agent.delegatedidentity.v1.DelegatedIdentity', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DelegatedIdentity(object):
    """The delegatedIdentity service provides an interface to get the SVIDs of other
    workloads on the host. This service is intended for use cases where a process
    (different than the workload one) should access the workload's SVID to
    perform actions on behalf of the workload. One example of is using a single
    node instance of Envoy that upgrades TCP connections for different processes
    running in such a node.

    The caller must be local and its identity must be listed in the allowed
    clients on the spire-agent configuration.
    """

    @staticmethod
    def SubscribeToX509SVIDs(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/spire.api.agent.delegatedidentity.v1.DelegatedIdentity/SubscribeToX509SVIDs',
            spire_dot_api_dot_agent_dot_delegatedidentity_dot_v1_dot_delegatedidentity__pb2.SubscribeToX509SVIDsRequest.SerializeToString,
            spire_dot_api_dot_agent_dot_delegatedidentity_dot_v1_dot_delegatedidentity__pb2.SubscribeToX509SVIDsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubscribeToX509Bundles(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/spire.api.agent.delegatedidentity.v1.DelegatedIdentity/SubscribeToX509Bundles',
            spire_dot_api_dot_agent_dot_delegatedidentity_dot_v1_dot_delegatedidentity__pb2.SubscribeToX509BundlesRequest.SerializeToString,
            spire_dot_api_dot_agent_dot_delegatedidentity_dot_v1_dot_delegatedidentity__pb2.SubscribeToX509BundlesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
