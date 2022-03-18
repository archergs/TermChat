import socket
import os
from server import *
from client import *

(width, height) = os.get_terminal_size()

exit = False
iplist = []


def main():
    while exit == False:
        # clear the terminal window
        os.system('cls' if os.name == 'nt' else 'clear')
        print(" Welcome to TermChat ".center(width, "-"))
        print("Your local IP Address: " +
              socket.gethostbyname(socket.gethostname()))
        print("To exit, enter 'e'")
        print("Learn more about TermChat, enter 'i'")
        startChoice = input(
            "Are you hosting (h) or connecting to (c) a chat: ").lower()

        if(startChoice == 'e'):
            break
        elif(startChoice == 'h'):
            print("Starting server...")
            createServer()
        elif(startChoice == 'c'):
            ip = input("Enter the IP address of the host: ")
            startChat(ip)
        elif(startChoice == 'i'):
            print(
                "Welcome to TermChat, a simple chat application that lives in your terminal!")
            print(
                "TermChat is used to chat with other users on the same network as you. You can choose")
            print(
                "to host or connect to a chat, and all that is needed to get started is the local IP address")
            print(
                "of the host! Don't worry, TermChat guides you through the whole process.")
            input("\nPress enter to return to the main menu")
        else:
            print("invalid input")


if __name__ == "__main__":
    main()
