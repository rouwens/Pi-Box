import time
import socket
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
    print ("4 - Mediaserver (JellyFin")
    print ("5 - Mediaserver (PLEX")
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
    status = "empty"
    # Checken of de map bestaat
    check = os.path.isdir('/etc/apache2')

    if check != True:
        print ()
        print ("The webserver is not installed. Enter install to begin the installation")
        status = Fore.WHITE + "not installed" + Style.RESET_ALL

    print ()
    print ("Webserver")
    print ("------------------")
    print ("Status: "+ status)
    print () 
    print ("1 - List web directory")
    print ("2 - Web applications")
    print ("3 - Settings")
    print ()
    print ("4 - Return")
    print ("5 - Exit")

    choice = input()

    if choice == "1":
        print ()
        os.system ("ls /var/www/html")
        input("Press Enter to continue...")
        return webserver()
       
    elif choice == "2":
        webapps()
    
    elif choice == "3":
        print()

    elif choice == ("4"):
        return software()
    
    elif choice == ("5"):
        exit()
    
    elif choice == ("install"):
        os.system ("apt update -y && apt install apache2 -y")
        print ()
        print ("De webserver is installed")
        timer()
        return webserver()
    
    else:
        print ()
        print ("Input not reconized. Please try agian...")
        timer()
        return webserver()

def webapps ():
    print ()
    print ("WebApps")
    print ("-------")
    print ("Select an app that you want to install")
    print ("")
    print ("1 - Worpress")
    print ("2 - Joomla")
    print ("3 - Drupal")
    print ("4 - Owncloud")
    print ("5 - Nextcloud")
    print ("6 - Shifexec")
    print ("7 - PhpMyadmin")
    print ()
    print ("8 - Return")
    print ("9 - Exit")
    choice = input()

    if choice == "1":
        location = "empty"
        print()
        print ("What is the name of the folder where you are goining to install wordpress? Use . to install it in to the root folder of the webserver.")
        folder = input()
        
        if folder == ".":
            location = "/var/www/html"

        else:
            location = "/var/www/html/" + folder
        
        foldercheck = os.path.isdir('/var/www/html/'+folder)

        if foldercheck == True:
            print ()
            print ("Folder is not empty. If you proceed than the target folder will be removed. (y/n)")
            proceed = input()

            if proceed == "y" or "yes":
                os.system ("rm -r " +location)
            
            elif proceed == "n" or "no":
                print ()
                print ("Nothing is removed. Please try agian.")
                timer
                return webapps()

            else:
                print ("Nothing is removed. Please try agian.")
                timer
                return webapps()                         
        cms = "wordpress"
        dir()
        os.system ("./scripts/install/LAMP.bash")
        os.system ("./scripts/web-apps.bash %s %s"%cms, location)
        print ()
        ip = [l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] 
        if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), 
        s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, 
        socket.SOCK_DGRAM)]][0][1]]) if l][0][0]

        print ("Wordpress is installed.")
        print ("In a webbrowser go to http://"+ip+"/"+folder)
        print ("At the database secion use the following.")
        print ()
        print ("Database Name: wordpress")
        print ("Username: wordpress")
        print ("Password: welcome01")
        print ("Database Host: localhost")
        print ("Table Prefix: (Anything you like)") 
        print ()
        timer
        return webapps


    elif choice == "2":    
        print ()

    elif choice == "3":    
        print ()

    elif choice == "4":    
        print ()

    elif choice == "5":    
        print ()

    elif choice == "6":    
        print ()

    elif choice == "7":    
        print ()

    elif choice == "8":    
        print ()

    else:
        print ()
        print ("Choice not reconized. Please try again...")
        timer()
        return webapps()        
start()