from email import message
from multiprocessing.connection import Client
import socket
import threading


nombre = input("Ingrese su nombre de usuario:\n")
room = input("Ingrese el código de la sala:\n")

host = '127.0.0.1'
port = 55555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))



def listen_server():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == "@username":
                client.send(nombre.encode('utf-8'))
            elif message == "@room":
                client.send(room.encode('utf-8'))
            else:
                print(message)

        except:
            print("Ha ocurrido un error")
            client.close()
            break

def write_message():
    while True:
        message = f"{nombre}: {input()}  [Sala: {room}]"
        client.send(message.encode('utf-8'))


listen_thread = threading.Thread(target=listen_server)
listen_thread.start()

write_thread = threading.Thread(target=write_message)
write_thread.start()
