import grpc
import boomerCall_pb2_grpc, boomerCall_pb2

if __name__ == '__main__':
    with grpc.insecure_channel('172.18.77.243:4005') as channel:
        stub = boomerCall_pb2_grpc.BoomerCallServiceStub(channel)
        response = stub.EndBommer(boomerCall_pb2.EndBommerRequest(), timeout=15)
        print(response.message)
