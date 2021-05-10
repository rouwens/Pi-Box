import time
import colorama
from colorama import Fore, Style
import os


# Het standaard riegeltje wanneer het programma moet stoppen
def exit ():
    print ()
    print ("Bye, bye")
    time.sleep(2)

# Standaard tijd om te wachten tussen print regels
def timer ():
    time.sleep(2)

# Map waar die standaard heen moet (voor de zekerheid)
def dir ():
    os.system ("cd /opt/Pi-Box/")

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
    print ("2 - Webserver")
    print ("3 - Adguard Home (Adblocker)")
    print ("4 - Remove software")
    print ("5 - Update system")
    print ("")
    print ("6 - Return to main menu")
    print ("7 - Exit")
    choice = input()

    if choice == "1":
        print()
    
    elif choice == "2":
        webserver () 

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

# Het menu van de webserver
def webserver():
    print ()
    print ("Webserver")
    print ("------------------")
    print ("Status:")
    print () 
    print ("1 - List directory")
    print ("2 - Install web applications")
    print ()
    print ("3 - Return")
    print ("4 - Exit")

    # Checken of de map bestaat
    check = os.path.isdir('/etc/apache2')

    if check != True:
        print ()
        print ("The webserver is not installed. Enter install to begin the installation")

    choice = input()

    if choice == "1":
        os.system ("ls /var/www/root")
        return webserver()
       
    elif choice == "2":
        print ()

    elif choice == ("3"):
        return software()
    
    elif choice == ("4"):
        exit()
    
    elif choice == ("install"):
        dir()
        os.system ("./scripts/install/LAMP.bash")
        timer()
        return webserver()
    
    else:
        print ()
        print ("Input not reconized. Please try agian...")
        timer()
        return webserver()
    
start()