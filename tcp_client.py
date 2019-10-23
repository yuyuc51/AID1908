import socket

HOST = "localhost"
PORT = 8888
BUFSIZ = 1024
ADDR = (HOST,PORT)

fd = socket.socket()
fd.connect(ADDR)

while True:
    data = input(">")
    if not data:
        break
    fd.send(data.encode())
    data = fd.recv(BUFSIZ)
    if not data:
        break
    print(data.decode())
fd.close()