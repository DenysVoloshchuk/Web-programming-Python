import socket
from datetime import datetime

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind((socket.gethostname(), 1309))

serv.listen()


clientsocket, address = serv.accept()
msg = clientsocket.recv(1024)
print(datetime.now(), ' > ', msg.decode("utf-8"))

