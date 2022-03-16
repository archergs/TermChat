import socket

host = 'localhost'
port = 5001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('', port))

s.listen(1)

c, addr = s.accept()

print("CONNECTION FROM:", str(addr))

c.send(b"Hello")

msg = "Cya"

c.send(msg.encode())

c.close()
