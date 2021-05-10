#!/bin/bash

apt update -y
apt -y install lsb-release apt-transport-https ca-certificates -y
wget -O /etc/apt/trusted.gpg.d/php.gpg https://packages.sury.org/php/apt.gpg
echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" | tee /etc/apt/sources.list.d/php.list
apt update -y
apt install apache2 mariadb-server php7.4 -y
