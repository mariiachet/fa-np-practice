import socket
from time import sleep

sock = socket.socket()
sock.setblocking(1)
sock.connect(('127.0.0.1', 9090))

#msg = input()
msg = "Hi!"
sock.send(msg.encode())

data = sock.recv(1024)

sock.close()

print(data.decode())
