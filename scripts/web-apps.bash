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
    cd /var/www/html
    apt install zip -y
    mkdir $2
    cd $2
    wget https://downloads.joomla.org/cms/joomla3/3-9-26/Joomla_3-9-26-Stable-Full_Package.zip
    unzip Joomla_3-9-26-Stable-Full_Package.zip
    rm Joomla_3-9-26-Stable-Full_Package.zip
    mysql -e "create database joomla"
    mysql -e "CREATE USER 'joomla'@'localhost' IDENTIFIED BY 'welcome01';"
    mysql -e "GRANT ALL PRIVILEGES ON joomla.* TO 'joomla'@'localhost';"
    mysql -e "FLUSH PRIVILEGES;"
    cd ../
    chmod 0777 -R $2
fi

if [ "$cms" == "drupal" ]; then
    cd /var/www/html
    wget https://www.drupal.org/download-latest/tar.gz
    tar xzf tar.gz 
    mv drupal-* $2
    rm tar.gz
    mysql -e "create database drupal"
    mysql -e "CREATE USER 'drupal'@'localhost' IDENTIFIED BY 'welcome01';"
    mysql -e "GRANT ALL PRIVILEGES ON drupal.* TO 'drupal'@'localhost';"
    mysql -e "FLUSH PRIVILEGES;"
    cd $2/sites/default/
    cp default.settings.php settings.php
    cd /var/www/html
    chmod 0777 -R $2
fi

