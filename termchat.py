import socket
import os
from server import *
from client import *

(width, height) = os.get_terminal_size()


def main():
    # clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')
    print(" Welcome to TermChat ".center(width, "-"))
    print("")
    startChoice = input("Are you hosting (h) or connecting to (c) a chat: ")

    if(startChoice == 'h'):
        print("Starting server...")
        createServer()
    elif(startChoice == 'c'):
        code = input("Enter the 5-digit code to enter a chat: ")
        startChat(code)
    else:
        print("invalid input")


if __name__ == "__main__":
    main()
