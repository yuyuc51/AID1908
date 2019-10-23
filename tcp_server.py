import socket
from time import ctime

HOST = "0.0.0.0"
PORT = 8888
BUFSIZ = 1024
ADDR = (HOST, PORT)

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(5)

while True:
    print("Wait connect from ...")
    fd, addr = s.accept()
    print("...connected from ", addr)

    while True:
        data = fd.recv(BUFSIZ)
        if not data:
            break
        # fd.send('OK'.encode())
        time = ctime()
        fd.send(b'%s'% time )
        print(data.decode())
    fd.close()

s.close()
