import grpc
from grpc_hello.proto import helloworld_pb2,helloworld_pb2_grpc

if __name__ == '__main__':
    with grpc.insecure_channel('127.0.0.1:3023') as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        rsp: helloworld_pb2.HelloReply = stub.Sayhello(helloworld_pb2.HelloRequest(name = "dagou"))
        print(rsp.message)