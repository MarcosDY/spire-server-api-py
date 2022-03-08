from http import client
from unicodedata import name
import grpc
import logging
from spire.api.server.trustdomain.v1 import trustdomain_pb2_grpc
from spire.api.server.trustdomain.v1 import trustdomain_pb2
from spire.api.types import federationrelationship_pb2
from pyspiffe.workloadapi.default_workload_api_client import DefaultWorkloadApiClient

_LOGGER = logging.getLogger(__name__)

def main():
    client = DefaultWorkloadApiClient('unix:///tmp/spire-agent/public/api.sock')
    svid = client.fetch_x509_svid()
    print(svid)
    with grpc.secure_channel('127.0.0.1:8081', svid.leaf) as channel:
    # with grpc.insecure_channel('unix:///tmp/spire-server/private/api.sock') as channel:
        stub = trustdomain_pb2_grpc.TrustDomainStub(channel)

        # print('Create federation relationship')
        # req = trustdomain_pb2.BatchCreateFederationRelationshipRequest()
        # fr = req.federation_relationships.add()
        # fr.trust_domain = "domain.test3"
        # fr.bundle_endpoint_url = "https://upstream-spire-server"
        # fr.https_spiffe.endpoint_spiffe_id = "spiffe://domain.test3/spire/server"

        # createResp = stub.BatchCreateFederationRelationship(req)
        # print(createResp)

        print('List federation')
        resp = stub.ListFederationRelationships(trustdomain_pb2.ListFederationRelationshipsRequest())
        print(resp)
if __name__ == '__main__':
    main()