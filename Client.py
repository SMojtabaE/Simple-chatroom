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


def receive():
    while True:
        try:
            massage = client.recv(1024).decode(FORMAT)
            if massage == "username":
                client.send(username.encode(FORMAT))
            else:
                print(massage)
        except:
            print("there is somthing Wrong!")
            client.close()
            break

        
def write():
    while True:
        massage = input("('leave'->exit):")
        if massage == DISCONNET_MSG:
            client.send(DISCONNET_MSG.encode(FORMAT))
            print ("you enterd leav!!!")
            input(" ")
            break 
        else:
            msg = f'{username}: {massage}'
            client.send(msg.encode(FORMAT))