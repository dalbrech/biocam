#!/bin/bash
sudo systemctl stop  motioneye
python3 /home/pi/RaspberryPi/Motorized_Focus_Camera/Autofocus.py
sudo systemctl start motioneye

