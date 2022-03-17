import socket

host = 'localhost'
port = 5001


def startChat(chatCode):

    s = socket.socket(socket.AF_INET,
                      socket.SOCK_STREAM)

    s.connect(('127.0.0.1', port))

    s.send(str.encode(chatCode))

    msg = s.recv(1024)

    while msg:
        receiveStr = msg.decode()

        if receiveStr == "exitnow":
            break

        print('Received:' + receiveStr)
        response = str.encode(input("Enter response: "))
        s.send(response)
        msg = s.recv(1024)

    s.close()
