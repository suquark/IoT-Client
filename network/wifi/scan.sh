#!/usr/bin/env bash

if [ ! $1 ]; then
    iwlist wlan0 scan
else
    iwlist $1 scan
fi
