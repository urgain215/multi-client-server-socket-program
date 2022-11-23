from socket import *
import time

serverSocket = socket(AF_INET,SOCK_STREAM)

port = int(input("Enter the port number to bind to: "))

serverSocket.bind(("",port))

serverSocket.listen(3)
print("Server is listening...")

no = 0
connectionSocket = []
for i in range(100):
	connectionSocket.append(0);
	
for i in range(100):
	connectionSocket[i],addr = serverSocket.accept()
	no += 1
	print(f"Connected with {addr}.")
	
	currTemp = '34 degree Celsius'
	
	accept = input("Accept another connectin (Y/N): ")
	if(accept == 'Y' or accept == 'y'):
		continue
	else:
		break

send = input("Press 1 to broadcast and 0 to terminate all connection: ")
if(send == '0'):
	for j in range(no):
		connectionSocket[j].close()
else:
	for j in range(no):
		connectionSocket[j].send(currTemp.encode())
	
