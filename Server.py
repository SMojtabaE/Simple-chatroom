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
print(f"Server is up with [{SERVER}] ...")
