from http import client
import grpc
import logging
from spire.api.server.trustdomain.v1 import trustdomain_pb2_grpc
from spire.api.server.trustdomain.v1 import trustdomain_pb2

_LOGGER = logging.getLogger(__name__)

def main():
    with grpc.insecure_channel('unix:///tmp/spire-server/private/api.sock') as channel:
        stub = trustdomain_pb2_grpc.TrustDomainStub(channel)
        resp = stub.ListFederationRelationships(trustdomain_pb2.ListFederationRelationshipsRequest())
        print(resp)

if __name__ == '__main__':
    main()