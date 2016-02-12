#!/usr/bin/env bash

echo "WARNING: You will go the setup routine. Please make sure that you are the closest user."
wpa_supplicant -B -P /run/wpa_supplicant.wlan0.pid -i wlan0 -D nl80211,wext -c wpa_supplicant.conf