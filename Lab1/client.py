from ctypes import sizeof
import socket

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.connect((socket.gethostname(), 1309))

while True:
    msg = input("Text your massage to server: ")
    if msg == 'stop':
        serv.send(msg.encode())
        break
    serv.send(msg.encode())
    msg = serv.recv(1024)
    print(msg.decode('utf-8'))
