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

if [ "$cms" == "owncloud" ]; then
    cd /var/www/html
    wget https://download.owncloud.org/community/owncloud-complete-20210326.tar.bz2
    tar xzf https://download.owncloud.org/community/owncloud-complete-20210326.tar.bz2
    mv owncloud $2
    chmod 0777 -R $2
    rm owncloud-complete-20210326.tar.bz2
    mysql -e "create database owncloud"
    mysql -e "CREATE USER 'owncloud'@'localhost' IDENTIFIED BY 'welcome01';"
    mysql -e "GRANT ALL PRIVILEGES ON owncloud.* TO 'owncloud'@'localhost';"
    mysql -e "FLUSH PRIVILEGES;"
fi

if [ "$cms" == "nextcloud" ]; then
    cd /var/www/html
    mkidr $2
    cd $2
    wget https://download.nextcloud.com/server/installer/setup-nextcloud.php
    mv setup-nextcloud.php setup.php
    cd ../
    chmod 0777 -R $2
    mysql -e "create database nextcloud"
    mysql -e "CREATE USER 'nextcloud'@'localhost' IDENTIFIED BY 'welcome01';"
    mysql -e "GRANT ALL PRIVILEGES ON nextcloud.* TO 'nextcloud'@'localhost';"
    mysql -e "FLUSH PRIVILEGES;"
fi

if [ "$cms" == "shiftexec" ]; then
    echo "Test"
    
fi

if [ "$cms" == "phpmyadmin" ]; then
    apt install zip -y
    cd /var/www/html
    wget https://files.phpmyadmin.net/phpMyAdmin/5.1.0/phpMyAdmin-5.1.0-all-languages.zip
    unzip phpMyAdmin-5.1.0-all-languages.zip
    rm phpMyAdmin-5.1.0-all-languages.zip
    mv phpMyAdmin-5.1.0-all-languages $2
fi