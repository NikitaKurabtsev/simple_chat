import socket


server_socket = socket.socket()
server_host = socket.gethostname()
ip = socket.gethostbyname(server_host)
server_port = 8080

print("This is your ip adress: ", ip)

server_host = input("Enter friend/'s IP Address: ")
name = input("Input your name: ")

server_socket.connect((server_host, server_port))

server_socket.send(name.encode())
server_name = server_socket.recv(1024).decode()

print(server_name, " Has joined...")

while True:
    message = server_socket.recv(1024).decode()
    print(server_name, ":", message)
    message = input("Me: ")
    if not message:
        break
    server_socket.send(message.encode())
