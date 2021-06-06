#!/bin/bash

apt update
apt install snapd -y
snap install core; sudo snap refresh core
snap install --classic certbot
ln -s /snap/bin/certbot /usr/bin/certbot
certbot --apache