
# Nathan Dallmann      


import os
import subprocess
import time

inpt = "temp"
defgate = "192.168.1.254"
RIT = "129.21.3.17"
dnstest = "www.google.com"

while True:
    # clears terminal and prints welcome text
    os.system("clear")
    print("Welcome to the Network Connectivity Test: \nPlease select the number of which option you'd like to test: \n1. Test default gateway: \n2. Test remote IP address: \n3. Test URL: \n4. Quit: \n")
    inpt = input("")
    # menu is simple, input the number that corresponds with the option you want. anything else is rejected


    # quits program
    if inpt == "4":
        print("Have a nice day: ")
        break


    # ping test for the default gateway
    # added extra input to each option, due to it skipping back to the beggining of the while loop and not printing the pin results
    elif inpt == "1":
        subprocess.run(["ping","-c","3",defgate])
        temp = input("Press enter to return to the menu:")


    # ping test for the remote IP address
    elif inpt == "2":
        subprocess.run(["ping","-c","3",RIT])
        temp = input("Press enter to return to the menu:")


    # ping test for the dns
    elif inpt == "3":
        subprocess.run(["ping","-c","3",dnstest])
        temp = input("Press enter to return to the menu:")


    # anything else is rejected and sent back to the beggining of the loop
    else:
        print("Invalid command. Please input a number from the list above: \n")
        temp = input("Press enter to return to the menu:")
	


