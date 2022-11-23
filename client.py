from socket import *
import time

clientSocket = socket(AF_INET,SOCK_STREAM)

ip = input("Enter the server's ip: ")
port = int(input("Enter the port to connect to: "))

clientSocket.connect((ip,port))

response = clientSocket.recv(2048)

decodeResponse = response.decode()

print(f"Current Temperature given by server is: {decodeResponse}.")



