import socket

host = 'localhost'
port = 5001

s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)

s.connect(('127.0.0.1', port))

msg = s.recv(1024)

while msg:
    print('Received:' + msg.decode())
    msg = s.recv(1024)

s.close()
