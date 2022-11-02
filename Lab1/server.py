import socket
import threading

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind((socket.gethostname(), 1309))

serv.listen()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames [index]
            broadcast(f' {nickname} left the chat!' .encode('ascii'))
            nicknames.remove(nickname)
            break

def receive():
    while True:
        client, address = serv.accept()
        print(f"connected with {str(address)}")
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)
        print(f'Nickname of the client is {nickname}')
        broadcast(f'{nickname} joined the chat!'.encode('ascii'))
        client.send(f'Connected to the server!'.encode('ascii'))
        if len(clients) == 0:
            serv.close()
            break
        thread = threading.Thread(target=handle, args=(client, ))
        thread.start()

print('Server has started')
receive()

