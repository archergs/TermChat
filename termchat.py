import socket
import os
from server import *
from client import *
from ping import *

(width, height) = os.get_terminal_size()

exit = False
iplist = []


def main():
    # clear the screen
    #os.system('cls' if os.name == 'nt' else 'clear')

    # map the network and get a list of ip addresses
    #print("Finding network devices, this may take a moment...")
    #iplist = map_network()

    while exit == False:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(" Welcome to TermChat ".center(width, "-"))
        print("")
        print("To exit, enter 'e'")
        startChoice = input(
            "Are you hosting (h) or connecting to (c) a chat: ")

        if(startChoice == 'e'):
            break
        elif(startChoice == 'h'):
            print("Starting server...")
            createServer()
        elif(startChoice == 'c'):
            ip = input("Enter the IP address of the host: ")
            startChat(ip)
        else:
            print("invalid input")


if __name__ == "__main__":
    main()
