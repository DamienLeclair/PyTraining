__author__ = 'dleclair'

# -------
# sockets
# -------

# import socket
#
# host = ''
# port = 12800
#
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_socket.bind((host, port))
# server_socket.listen(5)
# print("Server is listening on port {}".format(port))
#
# client_socket, client_info = server_socket.accept()
#
# recv_msg = b""
# while recv_msg != b"end":
#     recv_msg = client_socket.recv(1024)
#     print(recv_msg.decode())
#     client_socket.send(b"5 / 5")
#
# print("Closing connection")
# client_socket.close()
# server_socket.close()

import socket
import select

host = ''
port = 12800

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(5)
print("Server is listening on port {}".format(port))

is_server_running = True
connected_clients = []
while is_server_running:
    # On va vérifier que de nouveaux clients ne demandent pas à se connecter
    # Pour cela, on écoute la connexion_principale en lecture
    # On attend maximum 50ms
    new_client_connections, wlist, xlist = select.select([server_socket],
        [], [], 0.05)

    for new_connection in new_client_connections:
        client_socket, client_info = new_connection.accept()
        # On ajoute le socket connecté à la liste des clients
        connected_clients.append(client_socket)

    # Maintenant, on écoute la liste des clients connectés
    # Les clients renvoyés par select sont ceux devant être lus (recv)
    # On attend là encore 50ms maximum
    # On enferme l'appel à select.select dans un bloc try
    # En effet, si la liste de clients connectés est vide, une exception
    # Peut être levée
    clients_to_read = []
    try:
        clients_to_read, wlist, xlist = select.select(connected_clients,
                [], [], 0.05)
    except select.error:
        pass
    else:
        for client in clients_to_read:
            recv_msg = client.recv(1024)
            recv_msg = recv_msg.decode()
            print("Received {}".format(recv_msg))
            client.send(b"5 / 5")
            if recv_msg == "end":
                is_server_running = False

print("Closing connections")
for client in connected_clients:
    client.close()

server_socket.close()