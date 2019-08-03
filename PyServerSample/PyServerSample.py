# see: https://grpc.io/docs/quickstart/python/

# Generate gRPC code
# python -m grpc_tools.protoc -I../gRPCSample --python_out=. --grpc_python_out=. ../gRPCSample/Sample.proto

from concurrent import futures
import time

import grpc

import Sample_pb2
import Sample_pb2_grpc

class Sample(Sample_pb2_grpc.UserServiceServicer):

    def SetUser(self, request, context):
        print(request.id);
        print(request.name);
        return Sample_pb2.UserResponse(result=True)

server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
Sample_pb2_grpc.add_UserServiceServicer_to_server(Sample(), server)
server.add_insecure_port('[::]:50051')
server.start()

try:
    while True:
        time.sleep(60 * 60 * 24)
except KeyboardInterrupt:
    server.stop(0)
