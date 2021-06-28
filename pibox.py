import time
import socket
from colorama import Fore, Style
import os


# Het scherm schoon vegen
def clear (): 
    os.system("clear")

# Het standaard riegeltje wanneer het programma moet stoppen
def exit ():
    print ()
    print ("Bye, bye")
    time.sleep(2)
    exit

# Standaard tijd om te wachten tussen print regels
def timer ():
    time.sleep(2)

# Map waar die standaard heen moet (voor de zekerheid)
def dir ():
    os.system ("cd /opt/Pi-Box/")

# Het standaard riegelte bij verkeerde input
def wronginput ():
    print ()
    print ("Input not recognized. Please try it agian...")

# Het verkrijgen van het IP adres van de machine
ip = [l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] 
if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), 
s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, 
socket.SOCK_DGRAM)]][0][1]]) if l][0][0]

#Het start menu
def start (ip):
    clear()
    ip = ip
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
        software(ip)
    
    elif choice == "3":
        exit()
    
    else:
        wronginput ()
        time.sleep(2)
        return start()

def system():
    print ("System function")
    return start()

# Hoofdmenu van het onderdeel software
def software(ip):
    clear()
    ip = ip
    print ("Software")
    print ("----------")
    print ()
    print ("1  - View installed/running software")
    print ()
    print ("2  - Webserver")
    print ("3  - Adguard Home       (Adblocker)")
    print ("4  - Jellyfin           (mediaserver)")
    print ("5  - Transmission       (torrentserver)")
    print ("6  - Unifi controller")
    print ("7  - Kodi*              (Mediacenter)")
    print ("8  - Minecraft server*  (MineOS)")
    print ("9  - VPN                (OpenVPN)")
    print ("10 - Magic Mirror")
    print ("11 - Fileserver         (Samba)")
    print ("12 - Music library      (Subsonic)")
    print ("")
    print ("13 - Return to main menu")
    print ("14 - Exit")
    choice = input()

    if choice == "1":
        print()
    
    elif choice == "2":
        webserver (ip) 

    elif choice == "3":
        adguard (ip)
    
    elif choice == "4":
        jellyfin (ip)
    
    elif choice == "5":
        transmission(ip)
    
    elif choice == "6":
        unifi(ip)
    
    elif choice == "7":
        kodi(ip)
    
    elif choice == "8":
        minecraft(ip)
    
    elif choice == "9":
        vpn(ip)
    
    elif choice == "13":
        print ()
        return(software)
    
    elif choice == "14":
        exit()
    
    else:
        wronginput ()
        time.sleep(2)
        return software()

# Het menu van de webserver
def webserver(ip):
    clear()
    ip = ip
    status = "empty"
    # Checken of de map bestaat
    check = os.path.isdir('/etc/apache2')

    if check != True:
        print ()
        print ("The webserver is not installed. Enter install to begin the installation")
        status = Fore.WHITE + "not installed" + Style.RESET_ALL

    print ("Webserver")
    print ("------------------")
    print ("Status: "+ status)
    print () 
    print ("1 - List web directory")
    print ("2 - Web applications")
    print ("3 - Remove webapplication")
    print ("4 - Settings")
    print ()
    print ("5 - Return")
    print ("6 - Exit")
    print ()

    choice = input()

    if choice == "1":
        print ()
        os.system ("ls /var/www/html")
        input("Press Enter to continue...")
        return webserver()
       
    elif choice == "2":
        webapps(ip)
    
    elif choice == "3":
        print ("What's the name of the folder that you want to remove? A '.' stands for everything. Press on the 'c' key to cancel this operation.")
        folder = input ()

        if folder == ".":
            print ("Are you sure? (y/n)")
            choice = input()

            if choice == "y":
                os.system ("rm -r /var/www/html/*")
                print ("Everything is removed...")
                timer
            else:
                print ("Nothing is changed...")
                timer
            return webserver ()
        
        elif folder == "c":
            print ()
            print ("Operation canceld...")
            timer ()
            webserver ()
            
        print ("Are you sure that you want to remove " + folder + "? (y/n)")
        choice = input()

        if choice == "y":
            os.system ("rm -r /var/www/html/" +folder)
            print ("The folder is removed...")
            timer
            return webserver()
        else:
            print ("Operation cancceld...")
            timer
            return webserver()

    
    elif choice == "4":
        websettings ()

    elif choice == ("5"):
        return software()
    
    elif choice == ("6"):
        exit()
    
    elif choice == ("install"):
        dir()
        os.system ("./scripts/install/LAMP.bash")
        print ()
        print ("De webserver is installed")
        timer()
        return webserver()
    
    else:
        print ()
        wronginput ()
        timer()
        return webserver()

# Het menu van de instellingen voor de webserver
def websettings ():
    clear ()
    print ("Websettings")
    print ("-----------")
    print ("1 - Start service")
    print ("2 - Restart service")
    print ("3 - Stop service")
    print ()
    print ("4 - Change webserver port")
    print ("5 - HTTPS")
    print ("6 - Uninstall")
    print ()
    print ("7 - Return")
    print ()
    choice = input()

    if choice == "1":
        print ()
        os.system ("systemctl start apache2")
        print ("The webserver is starting...")
        timer ()
        websettings ()
    
    elif choice == "2":
        print ()
        os.system ("systemctl restart apache2")
        print ("The webserver is restarting...")
        timer ()
        websettings ()
    
    elif choice == "3":
        print ()
        os.system ("systemctl stop apache2")
        print ("The webserver has been stopped")
        timer ()
        websettings ()
    
    elif choice == "4":
        print ()
        print ("Which port do you want to user for the unsecure connection? (HTTP, default 80)")
        http = input()
        print ()
        print ("Which port do you want to user for the secured connection? (HTTPS, default 443)")
        https = input()
        print ()
        print ("Are you sure that you want to user these settings? (y/n")
        commit = input ()
        
        if commit == "y":
            print ()

        elif commit == "n":
            print ("Operation canceld...")
            timer ()
            websettings ()

        else:
            print ("Operation canceld...")
            timer ()
            websettings ()            

        os.system ("mv /etc/apache2/ports.conf /etc/apache2/ports.backup")
        os.system ("cp /etc/apache2/ports.original /etc/apache2/ports.conf")

        config_location = "/etc/apache2/ports.conf"
        config_location_new = "/etc/apache2/ports.temp"
        fin = open(config_location, "rt")
        fout = open(config_location_new, "wt")
        for line in fin:
            fout.write(line.replace('80', http))
        fin.close()
        fout.close()

        config_location = "/etc/apache2/ports.temp"
        config_location_new = "/etc/apache2/ports.conf"
        fin = open(config_location, "rt")
        fout = open(config_location_new, "wt")
        for line in fin:
            fout.write(line.replace('443', https))
        fin.close()
        fout.close()

        os.system("systemctl restart apache2")
        print ("Ports are changed")
        timer ()
        websettings ()

    
    elif choice == "5":
        print ()
        print ("Would you like to use a selfsigned certificate (s) or a free one from Certbot (c)? (s/c")
        print ("If you use one from Cerbot. Be sure that port 80 and 443 are open and you need a domainname.")
        print ()
        choice = input ()

        if choice == "s":
            print()
        
        elif choice == "c":
            print ()
            dir()
            os.system ("bash ./scripts/certbot.bash")
            print()
            print ("Certificate is installed")
            timer()
            websettings()

        
        else:
            print("Choice not recognized. Please try agian...")
            timer()
            websettings()
    
    elif choice == "6":
        print ()
        print ("Do you want to uninstall the webserver and database? Press than on the 'a' key. If you want to keep the webserver nor database, press than on the 'k' key")
        choice = input ()

        if choice == "a":
            print ()
            print ("Are you sure that you want to remove everything? (y/n)")
            choice = input ()

            if choice != "y":
                print ("Operation canceled")
                timer ()
                websettings ()
            
            os.system ("apt purge apache2-* php* mariadb-* -y ")
            print ()
            print ("All software is removed. The application files that are in the web folder are still there. Do you also remove these? (y/n)")
            choice = input ()

            if choice != "y":
                print ()
                print ("The files are not removed...")
                timer ()
                websettings ()
            
            os.system ("rm -r /var/www/html/*")
            print ()
            print ("Everythings is removed...")
            websettings ()
        
        elif choice == "k":
            print ()
            print ("Do you want to remove the webserver? (y/n")
            choice = input ()
            print ()

            if choice == "y":
                apache2 = "1"
            
            if choice == "n":
                apache2 = "0"
            
            else:
                print ("Input not reconized...")
                timer ()
                websettings ()
            
            print ("Do you want to remove the databaseserver? (y/n)")
            choice = input ()
            print ()

            if choice == "y":
                mariadb = "1"
            
            if choice == "n":
                mariadb = "0"
            
            else:
                wronginput ()
                timer ()
                websettings ()

            toberemoved = apache2 + mariadb

            if toberemoved == "00":
                print ("Nothing is removed.")
                timer ()
                websettings ()

            elif toberemoved == "10":
                os.system ("apt purge apache2-* php* -y")
                print ("The webserver is removed.")
                timer ()
                websettings ()

            elif toberemoved == "01":
                os.system ("apt purge mariadb-* -y")
                print ("The databaseserver is removed.")
                timer ()
                websettings
                
            elif toberemoved == "11":
                os.system ("apt purge apache2-* php* mariadb-* -y")
                print ("The webserver and database are removed.")
                timer ()
                websettings        
        
        else:
            wronginput ()
            timer ()
            websettings ()
    
    elif choice == "7":
        return webserver()   

# Het menu voor de web applicaties
def webapps (ip):
    ip = ip
    clear()
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
        print ("What is the name of the folder where you are goining to install Wordpress? Use . to install it in to the root folder of the webserver.")
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
                return webapps(ip)

            else:
                print ("Nothing is removed. Please try agian.")
                timer
                return webapps(ip)                         
        cms = "wordpress"
        dir()
        os.system ("./scripts/install/LAMP.bash")
        cmd = "./scripts/web-apps.bash %s %s"%(cms, location)
        os.system(cmd)
        print ()

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
        return webapps (ip)

    elif choice == "2":    
        location = "empty"
        print()
        print ("What is the name of the folder where you are goining to install Joomla? Use . to install it in to the root folder of the webserver.")
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
                return webapps(ip)                         
        cms = "joomla"
        dir()
        #os.system ("./scripts/install/LAMP.bash")
        cmd = "./scripts/web-apps.bash %s %s"%(cms, location)
        os.system(cmd)
        print ()

        print ("Joomla is installed.")
        print ("In a webbrowser go to http://"+ip+"/"+folder)
        print ("At the database secion use the following.")
        print ()
        print ("Host Name: localhost")
        print ("Username: Joomla")
        print ("Password: welcome01")
        print ("Database Name: Joomla")
        print ("Table Prefix: (Anything you like)") 
        print ()
        timer
        return webapps(ip) 

    elif choice == "3":    
        location = "empty"
        print()
        print ("What is the name of the folder where you are goining to install Drupal? Use . to install it in to the root folder of the webserver.")
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
                return webapps(ip)                         
        cms = "drupal"
        dir()
        #os.system ("./scripts/install/LAMP.bash")
        cmd = "./scripts/web-apps.bash %s %s"%(cms, location)
        os.system(cmd)
        print ()

        print ("Joomla is installed.")
        print ("In a webbrowser go to http://"+ip+"/"+folder)
        print ("At the database secion use the following.")
        print ()
        print ("Database name: drupal")
        print ("Database username: drupal")
        print ("Database password")
        print ()
        timer
        return webapps(ip) 

    elif choice == "4":    
        location = "empty"
        print()
        print ("What is the name of the folder where you are goining to install Owncloud? Use . to install it in to the root folder of the webserver.")
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
                return webapps(ip)                         
        cms = "owncloud"
        dir()
        #os.system ("./scripts/install/LAMP.bash")
        cmd = "./scripts/web-apps.bash %s %s"%(cms, location)
        os.system(cmd)
        print ()

        print ("Owncloud is installed.")
        print ("In a webbrowser go to http://"+ip+"/"+folder)
        print ()
        print ("You don't have to change the datafolder.")
        print ("At the database secion use the following.")
        print ()
        print ("User database: owncloud")
        print ("Password database: welcome01")
        print ("Name database: owncloud")
        timer
        return webapps(ip) 

    elif choice == "5":    
        location = "empty"
        print()
        print ("What is the name of the folder where you are goining to install Nextcloud? Use . to install it in to the root folder of the webserver.")
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
                return webapps(ip)                         
        cms = "nextcloud"
        dir()
        #os.system ("./scripts/install/LAMP.bash")
        cmd = "./scripts/web-apps.bash %s %s"%(cms, location)
        os.system(cmd)
        print ()

        print ("Nextcloud is installed.")
        print ("In a webbrowser go to http://"+ip+"/"+folder+"/setup.php")
        print ("For the install directory enter a . to install it")
        print ()
        print ("You don't have to change the datafolder.")
        print ("At the database secion use the following.")
        print ()
        print ("User database: nextcloud")
        print ("Password database: welcome01")
        print ("Name database: nextcloud")
        timer
        return webapps(ip) 

    elif choice == "6":    
        location = "empty"
        print()
        print ("What is the name of the folder where you are goining to install Shiftexec? Use . to install it in to the root folder of the webserver.")
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
                return webapps(ip)                         
        cms = "shiftexec"
        dir()
        #os.system ("./scripts/install/LAMP.bash")
        cmd = "./scripts/web-apps.bash %s %s"%(cms, location)
        os.system(cmd)
        print ()

        username = "shiftexec"
        password = "welcome01"
        config_location = location + "/config.rename_it.php"
        config_location_new = location + "/config.temp"
        fin = open(config_location, "rt")
        fout = open(config_location_new, "wt")
        for line in fin:
            fout.write(line.replace('my_username', username))
        fin.close()
        fout.close()

        config_location = location + "/config.temp"
        config_location_new = location + "/config.php"
        fin = open(config_location, "rt")
        fout = open(config_location_new, "wt")
        for line in fin:
            fout.write(line.replace('my_password', password))
        fin.close()
        fout.close()

        print ("Shiftexec is installed.")
        print ("In a webbrowser go to http://"+ip+"/"+folder)
        timer
        return webapps(ip) 

    elif choice == "7":    
        location = "empty"
        print()
        print ("What is the name of the folder where you are goining to install phpMyAdmin? Use . to install it in to the root folder of the webserver.")
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
                return webapps(ip)                         
        
              
        cms = "phpmyadmin"
        dir()
        #os.system ("./scripts/install/LAMP.bash")
        cmd = "./scripts/web-apps.bash %s %s"%(cms, location)
        os.system(cmd)
        print ()

        print ()
        print ("Do you want to connect phpMyAdmin to antoher MySQL/MariaDB server? If you don't know the answer press n. (y/n")
        remote = input ()

        if remote == "y":
            print ()
            print ("What will be the domainname/IP address?")
            address = input ()

            config_location = location + "/config.sample.inc.php"
            config_location_new = location + "/config.inc.php"
            fin = open(config_location, "rt")
            fout = open(config_location_new, "wt")
            for line in fin:
                fout.write(line.replace('localhost', address))
            fin.close()
            fout.close()
        
        print ()
        print ("phpMyAdmin is installed.")
        print ("In a webbrowser go to http://"+ip+"/"+folder)
        print ()
        timer
        return webapps(ip) 

    elif choice == "8":    
        return webserver ()

    elif choice == "9":
        exit()
    else:
        print ()
        print ("Choice not reconized. Please try again...")
        timer()
        return webapps(ip)        

# Het menu voor de adblocker
def adguard (ip):
    clear ()
    ip = ip
    status = "empty"
    # Checken of de map bestaat
    check = os.path.isdir('/opt/AdGuardHome')

    if check != True:
        print ()
        print ("AdGuard Home is not installed. Enter install to begin the installation")
        status = Fore.WHITE + "not installed" + Style.RESET_ALL

    print ("Adguard Home")
    print ("------------------")
    print ("Status: "+ status)
    print ()
    print ("1 - Start Adguard Home")
    print ("2 - Stop Adguard Home")
    print ("3 - Restart Adguard Home")
    print ("4 - Remove Adguard Home")
    print ()
    print ("5 - Return")
    print ("6 - Exit")

    choice = input()

    if choice == "1":
        os.system ("systemctl start AdGuardHome.service")
        return adguard(ip)

    elif choice == "2":
        os.system ("systemctl stop AdGuardHome.service")
        return adguard(ip)

    elif choice == "3":
        os.system ("systemctl restart AdGuardHome.service")
    
    elif choice == "4":
        clear()
        print ("Do you want to remove Adguard Home? (y/n)")
        choice = input()

        if choice == "y":
            clear()
            print ("Are you really sure? There is no going back after this point. (y/n)")
            choice = input ()

            if choice == "y":
                os.system("/opt/AdGuardHome/AdGuardHome -s uninstall")
                os.system("rm -r /opt/AdGuardHome")
                clear()
                print ("Adguard Home is removed...")
                timer ()

            elif choice == "n":
                clear()
                print ("Operation cancelled...")
                timer()
            
            else:
                clear()
                print("Input not recognized. Nothing is touched")
                timer()
            
            return adguard(ip)
    
    elif choice == "5":
        return software (ip)
    
    elif choice == "6":
        exit()
    
    elif choice == "install":
        clear()
        print ("Do you want to install Adguard Home? (y/n)")
        choice = input()
        clear()

        if choice == "y":
            os.system("apt update -y")
            os.system("apt install curl -y ")
            os.system("curl -s -S -L https://raw.githubusercontent.com/AdguardTeam/AdGuardHome/master/scripts/install.sh | sh -s -- -v")
            os.system("systemctl daemon-reload")
            clear()
            print ("In a webbrowser go to http://" + ip + ":3000 to finish the installation")
            input("Press Enter to continue...")
            return adguard(ip)

        elif choice == "n":
            print ("Operation cancelled")
            timer()
            return adguard(ip)

    else:
        wronginput()
        timer()
        return adguard (ip)

def jellyfin (ip):
    clear ()
    ip = ip
    status = "empty"
    # Checken of de map bestaat
    check = os.path.isdir('/etc/jellyfin')

    if check != True:
        print ()
        print ("Jellyfin is not installed. Enter install to begin the installation")
        status = Fore.WHITE + "not installed" + Style.RESET_ALL

    print ("Jellyfin")
    print ("------------------")
    print ("Status: "+ status)
    print ()
    print ("1 - Start Jellyfin")
    print ("2 - Stop Jellyfin")
    print ("3 - Restart Jellyfin")
    print ("4 - Remove Jellyfin")
    print ()
    print ("5 - Return")
    print ("6 - Exit")
    choice = input()
    print ()

    if choice == "1":
        os.system("systemctl start jellyfin.service")
        print ("Jellyfin is starting up...")
        timer()

    elif choice == "2":
        os.system("systemctl stop jellyfin.service")
        print ("Jellyfin is stopping...")
        timer()

    elif choice == "3":
        os.system("systemctl restart jellyfin.service")
        print ("Jellyfin is restarting...")
        timer()
    
    elif choice == "4":
        clear()
        print ("Do you want to remove Jellyfin? (y/n)")
        choice = input()

        if choice == "y":
            clear()
            print ("Are you really sure? There is no going back after this point. (y/n)")
            choice = input ()

            if choice == "y":
                os.system("apt purge jellyfin* -y")
                os.system("apt autoremove -y")
                os.system("rm -r /etc/jellyfin")
                clear()
                print ("Jellyfin is removed...")
                timer ()

            elif choice == "n":
                clear()
                print ("Operation cancelled...")
                timer()
            
            else:
                clear()
                print("Input not recognized. Nothing is touched")
                timer()
            
    elif choice == "5":
        software(ip)

    elif choice == "6":
        exit()
    
    elif choice == "install":
        clear()
        print ("Do you want to install Jellyfin? (y/n)")
        choice = input()
        print ()

        if choice == "y":
            os.system ("/opt/Pi-Box/scripts/install/jellyfin.bash")
            clear()
            print ("Jellyfin is installed. In a webbrowser go to http://" + ip + ":8096")
            input("Press Enter to continue...")
            return jellyfin(ip)

        if choice == "n":
            print ("Operation cancelled...")
            timer()
         
        else:
            print ("input not recognized..." )
            timer()
        
        return jellyfin(ip) 

    else:
        wronginput()
        timer()
        return jellyfin(ip)     

    return jellyfin(ip)

def transmission(ip):
    clear ()
    ip = ip
    status = "empty"
    # Checken of de map bestaat
    check = os.path.isdir('/etc/transmission-daemon')

    if check != True:
        print ()
        print ("Transmission is not installed. Enter install to begin the installation")
        status = Fore.WHITE + "not installed" + Style.RESET_ALL

    print ("Transmission")
    print ("------------------")
    print ("Status: "+ status)
    print ()
    print ("1 - Start Transmission")
    print ("2 - Stop Transmission")
    print ("3 - Restart Transmission")
    print ("4 - Remove Transmission")
    print ()
    print ("5 - Return")
    print ("6 - Exit")
    choice = input()
    print ()

    if choice == "1":
        os.system("systemctl start transmission-daemon.service")
        print ("Transmission is starting up...")
        timer()

    elif choice == "2":
        os.system("systemctl stop transmission-daemon.service")
        print ("Transmission is stopping...")
        timer()

    elif choice == "3":
        os.system("systemctl restart transmission-daemon.service")
        print ("Transmission is restarting...")
        timer()
    
    elif choice == "4":
        clear()
        print ("Do you want to remove Transmission? (y/n)")
        choice = input()

        if choice == "y":
            clear()
            print ("Are you really sure? There is no going back after this point. (y/n)")
            choice = input ()

            if choice == "y":
                os.system("apt purge transmission* -y")
                os.system("apt autoremove -y")
                os.system("rm -r /etc/transmission-daemon")
                clear()
                print ("Transmission is removed...")
                timer ()

            elif choice == "n":
                clear()
                print ("Operation cancelled...")
                timer()
            
            else:
                clear()
                print("Input not recognized. Nothing is touched")
                timer()
            
    elif choice == "5":
        software(ip)

    elif choice == "6":
        exit()
    
    elif choice == "install":
        clear()
        print ("Do you want to install Transmission? (y/n)")
        choice = input()
        print ()

        if choice == "y":
            os.system ("apt update")
            os.system ("apt install transmission-daemon -y")
            os.system ("systemctl stop transmission-daemon")

            fin = open("/etc/transmission-daemon/settings.json", "rt")
            #output file to write the result to
            fout = open("/etc/transmission-daemon/settings.json.temp", "wt")
            #for each line in the input file
            for line in fin:
                #read replace the string and write to output file
                fout.write(line.replace('"rpc-whitelist-enabled": true,', '"rpc-whitelist-enabled": false,'))
            #close input and output files
            fin.close()
            fout.close()

            os.system ("/etc/transmission-daemon/settings.json")
            os.system ("mv /etc/transmission-daemon/settings.json.temp /etc/transmission-daemon/settings.json")
            os.system ("systemctl start transmission-daemon")
            clear()
            print ("Transmission is installed. In a webbrowser go to http://" + ip + ":9091")
            print ("Use transmission for the username and password")
            print ()
            input("Press Enter to continue...")
            return transmission(ip)

        if choice == "n":
            print ("Operation cancelled...")
            timer()
         
        else:
            print ("input not recognized..." )
            timer()
        
        return transmission(ip) 

    else:
        wronginput()
        timer()
        return transmission(ip)     

    return transmission(ip)

def unifi (ip):
    clear ()
    ip = ip
    status = "empty"
    # Checken of de map bestaat
    check = os.path.isdir('/etc/unifi')

    if check != True:
        print ()
        print ("The Unifi Controller is not installed. Enter install to begin the installation")
        status = Fore.WHITE + "not installed" + Style.RESET_ALL

    print ("Unifi Controller")
    print ("------------------")
    print ("Status: "+ status)
    print ()
    print ("1 - Start Unifi Controller")
    print ("2 - Stop Unifi Controller")
    print ("3 - Restart Unifi Controller")
    print ("4 - Remove Unifi Controller")
    print ()
    print ("5 - Return")
    print ("6 - Exit")
    choice = input()
    print ()

    if choice == "1":
        os.system("systemctl start unifi.service")
        print ("unifi is starting up...")
        timer()

    elif choice == "2":
        os.system("systemctl stop unifi.service")
        print ("unifi is stopping...")
        timer()

    elif choice == "3":
        os.system("systemctl restart unifi.service")
        print ("unifi is restarting...")
        timer()
    
    elif choice == "4":
        clear()
        print ("Do you want to remove the Unifi Controller? (y/n)")
        choice = input()

        if choice == "y":
            clear()
            print ("Are you really sure? There is no going back after this point. (y/n)")
            choice = input ()

            if choice == "y":
                os.system("apt purge unifi* -y")
                os.system("apt autoremove -y")
                os.system("rm -r /etc/unifi")
                clear()
                print ("The Unifi controller is removed...")
                timer ()

            elif choice == "n":
                clear()
                print ("Operation cancelled...")
                timer()
            
            else:
                clear()
                print("Input not recognized. Nothing is touched")
                timer()
            
    elif choice == "5":
        software(ip)

    elif choice == "6":
        exit()
    
    elif choice == "install":
        clear()
        print ("Do you want to install the Unifi Controller? (y/n)")
        choice = input()
        print ()

        if choice == "y":
            os.system ("rm unifi-latest.sh &> /dev/null; wget https://get.glennr.nl/unifi/install/install_latest/unifi-latest.sh && bash unifi-latest.sh")
            clear()
            print ("The Unifi Controller is installed. In a webbrowser go to https://" + ip + ":8443")
            input("Press Enter to continue...")
            return unifi(ip)

        if choice == "n":
            print ("Operation cancelled...")
            timer()
         
        else:
            print ("input not recognized..." )
            timer()
        
        return unifi(ip) 

    else:
        wronginput()
        timer()
        return unifi(ip)     

    return unifi(ip)

def kodi(ip):
    print ()

def minecraft(ip):
    print ()

def vpn (ip):
    clear ()
    ip = ip
    status = "empty"
    # Checken of de map bestaat
    check = os.path.isdir('/etc/openvpn')

    if check != True:
        print ()
        print ("The VPN is not installed. Enter install to begin the installation")
        status = Fore.WHITE + "not installed" + Style.RESET_ALL

    print ("VPN")
    print ("------------------")
    print ("Status: "+ status)
    print ()
    print ("1 - Start VPN")
    print ("2 - Stop VPN")
    print ("3 - Restart VPN")
    print ("4 - Remove VPN")
    print ()
    print ("5 - Return")
    print ("6 - Exit")
    choice = input()
    print ()

    if choice == "1":
        os.system("systemctl start openvpn.service")
        print ("vpn is starting up...")
        timer()

    elif choice == "2":
        os.system("systemctl stop openvpn.service")
        print ("vpn is stopping...")
        timer()

    elif choice == "3":
        os.system("systemctl restart openvpn.service")
        print ("vpn is restarting...")
        timer()
    
    elif choice == "4":
        clear()
        print ("Do you want to remove vpn? (y/n)")
        choice = input()

        if choice == "y":
            clear()
            print ("Are you really sure? There is no going back after this point. (y/n)")
            choice = input ()

            if choice == "y":
                os.system("apt purge openvpn* -y")
                os.system("apt autoremove -y")
                os.system("rm -r /etc/openvpn")
                clear()
                print ("The VPN is removed...")
                timer ()

            elif choice == "n":
                clear()
                print ("Operation cancelled...")
                timer()
            
            else:
                clear()
                print("Input not recognized. Nothing is touched")
                timer()
            
    elif choice == "5":
        software(ip)

    elif choice == "6":
        exit()
    
    elif choice == "install":
        clear()
        print ("Do you want to install the VPN? (y/n)")
        choice = input()
        print ()

        if choice == "y":
            os.system ("cd /opt/Pi-Box/scripts && wget https://github.com/Nyr/openvpn-install/blob/master/openvpn-install.sh && mv openvpn-install.sh openvpn.sh")
            os.system ("/opt/Pi-Box/scripts/openvpn.sh")
            clear()
            print ("The VPN server is installed.")
            input("Press Enter to continue...")
            return vpn(ip)

        if choice == "n":
            print ("Operation cancelled...")
            timer()
         
        else:
            print ("input not recognized..." )
            timer()
        
        return vpn(ip) 

    else:
        wronginput()
        timer()
        return vpn(ip)     

    return vpn(ip)
    
start(ip)
