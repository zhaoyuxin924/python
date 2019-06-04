from socket import *
import time

bot_socket = socket(AF_INET,SOCK_STREAM)
bot_socket.bind(("127.0.0.1",10003))
bot_socket.listen(1024)
client_socket,client_addr = bot_socket.accept()


while True:
    recv_data = client_socket.recv(1024).decode().split(" ")
    recv_data.sort()
    print(recv_data)
    print(type(recv_data))
    time.sleep(10)

