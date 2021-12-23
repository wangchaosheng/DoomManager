from concurrent import futures
import grpc

from grpc_hello.proto import helloworld_pb2,helloworld_pb2_grpc

class Greeter(helloworld_pb2_grpc.GreeterServicer):
    def Sayhello(self, request, context):
        return helloworld_pb2.HelloReply(message= f'你好{request.name}')


if __name__ == '__main__':
    #实例化server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=50))
    #注册逻辑到server中
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(),server)
    #启动server
    server.add_insecure_port('127.0.0.1:3009')
    server.start()
    server.wait_for_termination()