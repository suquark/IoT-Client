#!/usr/bin/env bash

# For raspberrypi only
[ ! $1 ] && echo "Need new hostname" && exit

sudo sed -ri "s/127\.0\.1\.1.*/127\.0\.1\.1\t$1/g" /etc/hosts
sudo echo $1 > /etc/hostname
sudo /etc/init.d/hostname.sh
sudo service avahi-daemon restart