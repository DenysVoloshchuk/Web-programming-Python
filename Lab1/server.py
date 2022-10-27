import socket
from datetime import datetime
from time import sleep

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind((socket.gethostname(), 1309))

serv.listen()

clientsocket, address = serv.accept()
msg = clientsocket.recv(1024)
print(datetime.now(), ' > ', msg.decode('utf-8'))

sleep(5)

if  len(msg.decode('utf-8')) == len(msg):
    clientsocket.send((msg))
    print("All data sented succesfully")
else:
    print('Error')

clientsocket.close()

