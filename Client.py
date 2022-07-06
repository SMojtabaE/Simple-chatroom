import socket
import threading

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)
FORMAT = "utf-8"
DISCONNET_MSG = "leave"

username = input("enter your username : ")

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)