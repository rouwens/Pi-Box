import time
import colorama
from colorama import Fore, Style
import os


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
    print ("1 - View installed/running software")
    print ("2 - Install software")
    print ("3 - Manage software")
    print ("4 - Remove software")
    print ("5 - Update system")
    print ("")
    print ("6 - Return to main menu")
    print ("7 - Exit")
    choice = input()

    if choice == "1":
        software_installed()
    
    elif choice == "2":
        software_install()
    
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
def software_installed():
    apache2 = os.system('echo 3 | systemctl status apache2 >/dev/null 2>&1')
    apache2stat = 123

    if apache2 == 0:
        apache2stat = Fore.GREEN + "Running"

    elif apache2 == "1024":
        apache2stat = Fore.BLACK + "Not installed"

    else:
        apache2stat = Fore.RED + "Not running"
    print (apache2stat)
    print ()
    print ("Software - Installed/running")
    print ("---------------------")
    print ()
    print ("Webserver  " + apache2stat + Style.RESET_ALL)
    print ("Adblocker")

def software_install():
    print ()
    print ("Software - Install")
    print ("------------------") 
    print ("1 - Webserver")
    print ("2 - Adblocker")
    print ()
    print ("3 - Return")
    print ("4 - Exit")
    choice = input()

    if choice == "1":
        print ()
        print ("This will install the full Linux Apache2 Mariadb PHP (LAMP) stack")
        print ("Do you want to continue? (y/n")
        answer = input()
        if answer == "y":
            print ("Installing LAMP")
            print ("LAMP stack is installed")
            return software_install()
        elif answer == "n":
            return software_install()
        else:
            print ()
            print ("Unknow input. Please try again...")
            time.sleep(2)
            return software_install()
    
    if choice == "2":
        adblocker()
    
    if choice == ("3"):
        return software()
    
    if choice == ("4"):
        exit()
    
start()