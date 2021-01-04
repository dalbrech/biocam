#!/bin/bash

# Exit script if /mnt is not mounted somewhere
# Prevents filling the root filesystem (/)
#if ! mountpoint /mnt ; then
#    >&2 echo "Error: No mountpoint."
#    exit 1
#fi


SENSOR_LPS35HW=""

a=0


while (("$a" < "100")); do

if [ -f "/home/pi/sensorexamples/lps35hw.py" ]; then
        SENSOR_LPS35HW=`python3 /home/pi/sensorexamples/lps35hw.py`
fi
    name=`date +'%Y-%m-%d_%H%M%S_%3N'`
    #name=image$a.jpg
    sudo fswebcam -d /dev/video1 -r "640x480" --info "$SENSOR_LPS35HW Frame# $a $name" --fps 1 -F 1 -S 0  --save /home/pi/MicroscopeImages/$name.jpg 
    #sudo fswebcam -d /dev/video1 -r "1280x720" -F 1 -S 0 --save /home/pi/MicroscopeImages/$name 
    #echo Sleeping...
    #sleep  10
    let a++
done
#sudo ffmpeg -r 2 -i image-%04d.jpg -r 2 -vcodec libx264 -crf 20 -g 15 timelapse.avi
