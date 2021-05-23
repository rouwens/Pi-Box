#!/bin/bash

cms=$1 
 
if [ "$cms" == "wordpress" ]; then
    cd /var/www/html
    wget https://wordpress.org/latest.tar.gz
    tar xzf latest.tar.gz
    mv wordpress $2
    rm /var/www/html/latest.tar.gz
    apt install php7.4-{bcmath,bz2,intl,gd,mbstring,mysql,zip} -y
    systemctl restart apache2
    mysql -e "create database wordpress"
    mysql -e "CREATE USER 'wordpress'@'localhost' IDENTIFIED BY 'welcome01';"
    mysql -e "GRANT ALL PRIVILEGES ON wordpress.* TO 'wordpress'@'localhost';"
    mysql -e "FLUSH PRIVILEGES;"
    chmod 0777 -R $2
fi

if [ "$cms" == "joomla" ]; then
    echo "Joomla installed"
fi