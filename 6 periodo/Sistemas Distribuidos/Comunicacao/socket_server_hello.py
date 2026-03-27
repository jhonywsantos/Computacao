import socket

HOST = "localhost"
PORT = 5000


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)
print(f"Listen at port {PORT}")

conn, addr = server.accept()
print(f"Connected by {addr}")

#while(True):
data = conn.recv(1024)

print(f"Message: {data.decode()}")
  #conn.sendall("Hello world for you too".encode())