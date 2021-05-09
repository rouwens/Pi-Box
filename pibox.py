import time
import colorama
from colorama import Fore, Style


# Het standaard riegeltje wanneer het programma moet stoppen
def exit ():
    print ("Bye, bye")
    time.sleep(2)

#Het start menu
def start ():
    print ("#   _______  ___     _______  _______  __   __ ")
    print ("#  |       ||   |   |  _    ||       ||  |_|  |")
    print ("#  |    _  ||   |   | |_|   ||   _   ||       |")
    print ("#  |   |_| ||   |   |       ||  | |  ||       |")
    print ("#  |    ___||   |   |  _   | |  |_|  | |     | ")
    print ("#  |   |    |   |   | |_|   ||       ||   _   |")
    print ("#  |___|    |___|   |_______||_______||__| |__|")
    print ()
    print ()
    print ("1. System")
    print ("2. Software")
    print ()
    print ("3. Exit")
    print ()
    choice = input()

    if choice == "1":
        system()
    
    elif choice == "2":
        software()
    
    elif choice == "3":
        exit()
    
    else:
        print ("Input not recognized. Please do it again...")
        time.sleep(2)
        return start()

def system():
    print ("System function")
    return start()

# Hoofdmenu van het onderdeel software
def software():
    print()
    print ("Software")
    print ("----------")
    print ()
    print ("1 - View installed software")
    print ("2 - Install software")
    print ("3 - Manage software")
    print ("4 - Remove software")
    print ("5 - Update system")
    print ("")
    print ("6 - Return to main menu")
    print ("7 - Exit")
    choice = input

    if choice == "1":
        print ()
    
    elif choice == "2":
        print ()
    
    elif choice == "3":
        print ()
    
    elif choice == "4":
        print ()
    
    elif choice == "5":
        print()
    
    elif choice == "6":
        print ()
        return(software)
    
    elif choice == "7":
        exit()
    
    else:
        print ("Input not recognized. Please do it again...")
        time.sleep(2)
        return software()

# Laat software zien dat op het systeem is geinstalleerd       
def software-installed():
    print ()
    print ("Software - Installed")
    print ("---------------------")
    print ()
    print ("Webserver")
    print ("Adblocker")

def software-install():
    print()
start()