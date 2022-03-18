import socket

port = 6000
chatname = ""


def createServer():

    chatname = input("Enter your chatname: ")

    # Create the socket, for use on the local network
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    hostname = socket.gethostname()
    this_ip = socket.gethostbyname(hostname)
    print("Tell the client to enter " + this_ip + " to connect to chat")

    sock.bind(('', port))

    # only listen for one connection
    sock.listen(1)

    # accept a connection from the client
    connection, addr = sock.accept()

    print("CONNECTION FROM:", str(addr))

    receive = connection.recv(1024)

    connection.send(b"Chat connected")

    # now we can receive further msgs from the client
    receive = connection.recv(1024)

    while receive:
        receiveStr = receive.decode()

        # if the msg "exitnow" is received, close the connection
        if "exitnow" in receiveStr:
            connection.close()
            break

        print(receiveStr)
        response = input("Enter response: ")
        connection.send(str.encode(chatname + ": " + response))
        receive = connection.recv(1024)

    connection.close()
