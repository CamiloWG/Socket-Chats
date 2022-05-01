
import socket
import user, room
import threading



host = '127.0.0.1'
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))

server.listen()
print(f"- | - Server Online {host}:{port}")


AllUsers = []

def BroadcastToRoom(message, _room, author):
    for usuarios in _room.usersInRoom:
        if usuarios != author:
            usuarios.client.send(message)

def GetClientObject(client):
    for users in AllUsers:
        if users.client == client:
            return users

def ListenClient(client):
    _client = GetClientObject(client)
    while True:
        try:
            message = client.recv(1024)
            BroadcastToRoom(message, _client.roomObject, _client)
        except:
            BroadcastToRoom(f"- | - El usuario {_client.username} se desconectó [Room: {_client.inRoom}]".encode('utf-8'), _client.roomObject, _client)
            print(f"- | - El usuario {_client.username} se desconectó [Room: {_client.inRoom}]")
            _client.roomObject.RemoveUser(_client)
            AllUsers.remove(_client)
            client.close()
            break


def receive_connections():
    while True:
        client, adress = server.accept()

        client.send("@username".encode('utf-8'))
        name = client.recv(1024).decode('utf-8')

        client.send("@room".encode('utf-8'))
        roomId = int(client.recv(1024).decode('utf-8'))

        newUser = user.User(client, name, roomId, adress)
        AllUsers.append(newUser)

        room.SearchRoom(newUser, roomId)
        

        print(f"{name} connected [{adress}]")

        client.send("Connected to server".encode('utf-8'))

        thread = threading.Thread(target=ListenClient, args=(client,))
        thread.start()

receive_connections()

        
