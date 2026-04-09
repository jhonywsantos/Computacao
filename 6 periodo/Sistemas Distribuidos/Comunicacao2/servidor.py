from concurrent import futures
import grpc
import Hello_pb2
import Hello_pb2_grpc

class HelloServer(Hello_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        print(f'Message from {request.name}')
        return Hello_pb2.HelloReply(message="Alo, Mundo !")
def serve():
    port = '50001'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    Hello_pb2_grpc.add_GreeterServicer_to_server(HelloServer(), server)
    server.add_insecure_port('localhost:' + port)
    server.start()
    print(f'Server started and listening at port {port}')
    grpc.server.wait_for_termination()
if __name__ == '__main__':
    serve()