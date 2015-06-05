__author__ = 'dleclair'

import socket

host = "localhost"
port = 12800

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))
print("Connection established on port {}".format(port))

send_msg = b""
while send_msg != b"end":
    send_msg = input("> ")
    send_msg = send_msg.encode()
    client_socket.send(send_msg)
    recv_msg = client_socket.recv(1024)
    print(recv_msg.decode())

print("Closing connection")
client_socket.close()