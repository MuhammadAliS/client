  GNU nano 2.9.3                                                                   client.py                                                                             

import socket
c=socket.socket()
c.connect(('localhost',9922))
print("Connected to the network")
print(c.recv(1024).decode())
username=input("Enter a username:")
c.send(bytes(username,'utf-8'))
password=input("Enter a Password:")
c.send(bytes(password,'utf-8'))
i=c.recv(1024).decode()

while (i=='y'):
 chat=input("Client:") 
 c.send(bytes(chat,'utf-8'))
 chat=c.recv(1024).decode()
 print("Server:",chat)
 i=c.recv(1024).decode()





