import socket

HOST = "localhost" #Coloque aqui o IP do servidor
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
client.sendall((input("Envie uma mensagem: ")).encode())
#data = client.recv(1024)

#print(f"Received {data.decode()}")

client.close()