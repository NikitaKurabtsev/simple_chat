import socket
import time


server_socket = socket.socket()
host_name = socket.gethostname()
server_ip = socket.gethostbyname(host_name)
port = 8080

server_socket.bind((host_name, port))
print("Binding successful!")
print("This is your ip adress: " + server_ip)

name = input("Enter your name: ")
print("Waiting for client connection...")

server_socket.listen(1)

connection, address = server_socket.accept()

print("Received Connection from", address[0])
time.sleep(1)
print("...")
time.sleep(1)
print("...")
time.sleep(1)
print("Connection established. Connected from:", address[0])

client_name = connection.recv(1024).decode()
print(client_name + " has connected.")
connection.send(name.encode())

while True:
    message = input("Me: ")
    if not message:
        break

    connection.send(message.encode())
    client_message = connection.recv(1024).decode()
    print(client_name, ":", client_message)
