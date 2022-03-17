import socket
import this
import time

host = 'localhost'
port = 6000
chatname = ""


def startChat(ip):

    chatname = input("Enter your chatname: ")

    sock = socket.socket(socket.AF_INET,
                         socket.SOCK_STREAM)

    try:

        sock.connect((ip, port))
        sock.send(str.encode(ip))

        msg = sock.recv(1024)

        while msg:
            receiveStr = msg.decode()

            if "exitnow" in receiveStr:
                sock.close()
                break

            print(receiveStr)
            response = input("Enter response: ")
            sock.send(str.encode(chatname + ": " + response))
            msg = sock.recv(1024)

        sock.close()

    except ConnectionRefusedError:
        print("Connection refused")
        time.sleep(1)
        # return to main menu


def test_ip(sock, ip):
    try:
        sock.connect((ip, port))
        sock.close()
        return True
    except ConnectionRefusedError:
        return False
