import socket
import time

with socket.socket() as server_socket:
	host_name = input("Enter host address: ")
	port = int(input("Enter port: "))

	server_socket.bind((host_name, port))
	print("Binding successful!")
	print("This is your ip address:" + host_name)

	name = input("Enter your name: ")
	print("Waiting for client conn...")

	server_socket.listen(1)

	conn, address = server_socket.accept()

	print("Received conn from", address[0])
	time.sleep(1)
	print("...")
	time.sleep(1)
	print("...")
	time.sleep(1)
	print("conn established. conn from:", address[0])

	client_name = conn.recv(1024).decode()
	print(client_name + " has connected")
	conn.send(name.encode())

	while True:
		message = input("Me: ")
		if not message:
			break

		conn.send(message.encode())
		client_message = conn.recv(1024).decode()
		print(client_name, ":", client_message)
