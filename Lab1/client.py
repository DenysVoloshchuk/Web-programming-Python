from datetime import datetime
import socket
import threading

nickname = input('Enter a nickname: ')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((socket.gethostname(), 1309))


def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("An error occurred!")
            client.close()
            break

def write():
    while True:
        text = input('')
        if text.lower == 'exit':
            client.close()
            break
        message = f'{datetime.now()} | {nickname}: {text}'
        client.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()






# while True:
#     msg = input("Text your massage to server: ")
#     if msg == 'stop':
#         client.send(msg.encode())
#         break
#     client.send(msg.encode())
#     msg = client.recv(1024)
#     print(msg.decode('utf-8'))
