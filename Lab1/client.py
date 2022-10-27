from ctypes import sizeof
import socket

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.connect((socket.gethostname(), 1309))

msg = input("Text your massage to server: ")
serv.send(msg.encode())

msg = serv.recv(1024)
print(msg.decode('utf-8'))
