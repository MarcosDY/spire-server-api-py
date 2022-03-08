from http import client
from unicodedata import name
import grpc
import logging
from spire.api.server.trustdomain.v1 import trustdomain_pb2_grpc
from cryptography.hazmat.primitives import serialization
from spire.api.server.trustdomain.v1 import trustdomain_pb2
from spire.api.types import federationrelationship_pb2
from pyspiffe.workloadapi.default_workload_api_client import DefaultWorkloadApiClient

def main():
    client = DefaultWorkloadApiClient('unix:///tmp/spire-agent/public/api.sock')
    svid = client.fetch_x509_svid()
    leaf = svid.leaf().public_bytes(encoding=serialization.Encoding.PEM)
    print(leaf)
    print()
    # Never ever print PrivateKey, it is only for testing...
    privateKey = svid.private_key().private_bytes(serialization.Encoding.PEM, serialization.PrivateFormat.PKCS8, serialization.NoEncryption())
    print(privateKey)
    print()

    creds = grpc.ssl_channel_credentials(certificate_chain=leaf, private_key=privateKey)

    with grpc.secure_channel('127.0.0.1:8081', creds) as channel:
        stub = trustdomain_pb2_grpc.TrustDomainStub(channel)

        print('Create federation relationship')
        req = trustdomain_pb2.BatchCreateFederationRelationshipRequest()
        fr = req.federation_relationships.add()
        fr.trust_domain = "domain.test"
        fr.bundle_endpoint_url = "https://upstream-spire-server"
        fr.https_spiffe.endpoint_spiffe_id = "spiffe://domain.test3/spire/server"

        createResp = stub.BatchCreateFederationRelationship(req)
        print(createResp)

        print('List federation')
        resp = stub.ListFederationRelationships(trustdomain_pb2.ListFederationRelationshipsRequest())
        print(resp)
if __name__ == '__main__':
    main()