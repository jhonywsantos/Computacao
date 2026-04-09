from __future__ import print_function
import grpc
import Hello_pb2
import Hello_pb2_grpc
def run():
    print('Sending request message ...')
    channel = grpc.insecure_channel('localhost:50001')
    stub = Hello_pb2_grpc.GreeterStub(channel)
    response = stub.SayHello(Hello_pb2.HelloRequest(name='Jonny Bravo'))
    print(f'Server says {response.message}')
if __name__ == '__main__':
    print("Init the client")
    run()