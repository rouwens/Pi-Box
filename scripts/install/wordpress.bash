#!/bin/bash
cd /var/www/html
wget https://wordpress.org/latest.tar.gz
tar xzf latest.tar.gz
mv wordpress $1
