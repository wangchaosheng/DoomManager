# Walocust
     基于locust和boomer核心，使用基于etcd做为压测机服务发现。
     使用gRPC推送http请求事务描述信息，让压测机自己构造http接口测试任务。
     使用postman类似的界面管理http请求事务描述信息。
     搭配fastperfomance即可实现，任务隔离，历史执行记录管理，多人压测。

## 说明
     对locust1.3进行了二次开发，所有的接口方法全部兼容多人压测模式，locust源码对runner类进行大量修改以支持多人模式，boomer这边新增了一个csv导入功能

         
## 启动参考：这里的ip、port都是例子，请根据实际情况设置
  ### 1-先下载etcd并在服务器上启动etcd：
  etcd下载地址： https://github.com/etcd-io/etcd/releases/download/v3.3.25/etcd-v3.3.25-windows-amd64.zip  
  	etcd.exe --listen-client-urls http://0.0.0.0:2379 --advertise-client-urls http://0.0.0.0:2379
       
  ### 2-在服务器上启动matser（假定服务器ip：192.168.23.222）：
  #### python3-pip安装：
    pip install grpcio
    pip install grpcio-tools
    pip install etcd3
    pip install locust==1.2.3
  #### 启动命令：
    python3 main.py --master-host=192.168.23.222 [--step-load]
  ### 3-压力器上，可以直接从web页面的压测机管理下载编译好的执行程序（windows64，及linux64）
  压力器上，执行此程序（假定etcd的ip：192.168.23.222）
      boomerHazardServer -EtcdAddr 192.168.23.222:2379 [-Host 压力器自己的ip] [-Port 3000]
    
## master端提供了编译好的worker端，如果想要自己编译woker端，阅读以下内容
 #### 1-golang：采用了go mod管理包，get的包默认在[gopath]/pkg/mod中
 #### 2-如果需要重新生成pb：
- 1- 需要先安装proto工具，注意对应protoc-gen-go需要v1.3.2)：
       进入pkg\mod\github.com\golang\protobuf@v1.3.2，执行build命令生成执行文件protoc-gen-go，并替换GOPATH下bin/protoc-gen-go(与protoc同一个目录)
- 2-在proto文件夹下，执行命令生成pb文件：protoc --go_out=plugins=grpc:. *.proto --python_out=.
- 3-在页面上提交事务，worker会遇到报错：error gomq/zmtp: Got error while receiving greeting: Version 3.0 received does match expected version 3.1 
     解决方法：修改 mod\github.com\zeromq\gomq\zmtp\protocol.go 中的minorVersion uint8 = 1 改成 0
#### 3-编译，根据操作系统(windows,linux)编译对应压测机（worker）端应用程序：
  	go build boomerHazardServer.go
  	注：Windows编译linux，先在cmd执行set GOOS=linux 以及 set GOARCH=amd64
  
 
## 部分代码摘抄和参考了网络上的文章，致谢
   go-etcd-grpc :"https://www.cnblogs.com/wujuntian/p/12838041.html"
   
