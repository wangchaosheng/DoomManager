from protobuf_test.proto import hello_pb2

request = hello_pb2.HelloRequest()
request.name = "bobby"
res_Str = request.SerializeToString()
print(res_Str)

#如何通过字符串反向生成对象
request2 = hello_pb2.HelloRequest()
request2.ParseFromString(res_Str)
print(request2.name)