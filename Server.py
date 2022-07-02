import threading
import socket

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)
FORMAT = "utf-8"
DISCONNECT_MSG = "!leave"


server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind(ADDR)
server.listen()

clients = {}

def broadcast(msg):
    for client in clients:
        client.send(msg)

def handle(client):
    pass


def receive():
    while True :
        client,addr = server.accept()
        print(f"[{addr}] Connected")

        client.send("username".encode(FORMAT))
        username = client.recv(100).decode(FORMAT)
        clients[client] = username

        broadcast(f"{username} joined the chat!".encode(FORMAT))
        client.send("connected to the chat".encode(FORMAT))

        try:
            thread = threading.Thread(target=handle,args=(client,))
            thread.start()
        except:
            print("somthing went wrong!!!")

print(f"Server is up with [{SERVER}] ...")
