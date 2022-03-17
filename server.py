import socket
import random

host = 'localhost'
port = 5001


def createServer():

    connectCode = str(random.randint(10000, 99999))
    print("Use " + connectCode + " to connect to chat")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind(('', port))

    s.listen(1)

    c, addr = s.accept()

    print("CONNECTION FROM:", str(addr))

    receive = c.recv(1024)
    
    if receive.decode() == connectCode:
        c.send(b"Chat connected")

        receive = c.recv(1024)

        while receive:
            receiveStr = receive.decode()

            if receiveStr == "exitnow":
                break

            print('Received:' + receiveStr)
            response = str.encode(input("Enter response: "))
            c.send(response)
            receive = c.recv(1024)

    c.close()
