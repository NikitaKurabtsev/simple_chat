from email import message
import socket


with socket.socket() as client_socket:
    server_host = input("Enter server host: ")
    server_port = int(input("Enter server port: "))
    
    name = input("Input your name: ")

    client_socket.connect((server_host, server_port))

    client_socket.send(name.encode())
    server_name = client_socket.recv(1024).decode()

    print(server_name, " Has joined...")

    while True:
        message = client_socket.recv(1024).decode()
        if not message:
            break
        print(server_name, ":", message)
        message = input("Me: ")
        if not message:
            break
        client_socket.send(message.encode())
