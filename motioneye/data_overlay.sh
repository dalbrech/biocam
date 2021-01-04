#!/bin/sh
CAM_CONFIG_FILE="/etc/motioneye/camera-1.conf"
CAM_NAME=''
if [ -f $CAM_CONFIG_FILE ]; then
	CAM_NAME=`grep text_left $CAM_CONFIG_FILE | cut -f2 -d' '`
fi
TEMP=`vcgencmd measure_temp | cut -f2 -d'='`
VOLT=`vcgencmd measure_volts | cut -f2 -d'='`
SPEED=`vcgencmd measure_clock arm | cut -f2 -d'='`
LEN=`expr length $SPEED`
SPEED=`echo $SPEED | cut -c 1-$(($LEN-6))`
#SPEED=${SPEED%%"000"}
LOAD=`uptime | cut -f3- -d, | cut -f2 -d:`

WIFISPEED=`sudo iwconfig wlan0 | grep "Bit Rate" | cut -f2 -d'=' | cut -f1 -d'T'`
WIFISIGNAL=`sudo iwconfig wlan0 | grep "Signal" | cut -f3 -d'='`

###########################
#
OTHERDATA=""
if [ -f "/etc/motioneye/temp_hum.py" ]; then
        SENSOR=`python3 /etc/motioneye/temp_hum.py | grep "Temp"`
	OTHERDATA=$SENSOR
	#SENSORT=`echo $SENSOR | grep "*C"`
        #SENSORH=`echo $SENSOR | grep "Hum"`
        #OTHERDATA=$SENSORT$SENSORH
fi




SENSOR_AS726=""
#AS726x 6 channel visible light sensor 
if [ -f "/home/pi/sensorexamples/as726.py" ]; then
        SENSOR_AS726=`python3 /home/pi/sensorexamples/as726.py`
fi


SENSOR_TSL2591=""
#TSL light sensor 
if [ -f "/home/pi/sensorexamples/tsl2591.py" ]; then
        SENSOR_TSL2591=`python3 /home/pi/sensorexamples/tsl2591.py`
	
	
fi


SENSOR_MPRLS=""
#MPRLS ported pressure sensor 
if [ -f "/home/pi/sensorexamples/mprls.py" ]; then
        SENSOR_MPRLS=`python3 /home/pi/sensorexamples/mprls.py`
	
	
fi


SENSOR_LPS35HW=""
#MPRLS ported pressure sensor 
if [ -f "/home/pi/sensorexamples/lps35hw.py" ]; then
        SENSOR_LPS35HW=`python3 /home/pi/sensorexamples/lps35hw.py`
	
	
fi

SENSOR_SGP30=""
#SGP30 Gas  sensor 
if [ -f "/home/pi/sensorexamples/sgp30.py" ]; then
       SENSOR_SGP30=`python3 /home/pi/sensorexamples/sgp30.py`
	
	
fi

SENSOR_MCP9808=""
#MCP9808 temperature sensor 
if [ -f "/home/pi/sensorexamples/mcp9808.py" ]; then
        SENSOR_MCP9808=`python3 /home/pi/sensorexamples/mcp9808.py`
	
	
fi

SENSOR_BME280=""
#BME280 temperature and pressure sensor 
if [ -f "/home/pi/sensorexamples/bme280.py" ]; then
        SENSOR_BME280=`python3 /home/pi/sensorexamples/bme280.py`
	
	
fi
OTHERDATA=$SENSOR_AS726"\n"$SENSOR_TSL2591"\n"$SENSOR_MPRLS"\n"$SENSOR_LPS35HW"\n"$SENSOR_SGP30"\n"$SENSOR_MCP9808"\n"$SENSOR_BME280

#OTHERDATA="\n Temp: xx.x'C\n  Hum: xx.x\n   pH: xx.x\n  CO2: xx\n   O2: xx"
#
###########################

#CPU="$CAM_NAME\%20$TEMP\%20$VOLT\%20$SPEED\MHz"
CPU="$CAM_NAME\%20$TEMP\%20Load$LOAD"
WIFI="WiFi:  $WIFISIGNAL\%20$WIFISPEED"
echo "$OTHERDATA\n$CPU\n$WIFI"
#echo "$CPU\n$WIFI"

curl "http://localhost:7999/1/config/set?text_left=$OTHERDATA\n$CPU\n$WIFI"
#curl "http://localhost:7999/1/config/set?text_left=$CAM_NAME\%20$TEMP$OTHERDATA"

SENSOR_AS726_VIOLET=`echo $SENSOR_AS726 | cut -f6 -d" "`
SENSOR_AS726_BLUE=`echo $SENSOR_AS726 | cut -f8 -d" "`
SENSOR_AS726_GREEN=`echo $SENSOR_AS726 | cut -f10 -d" "`
SENSOR_AS726_YELLOW=`echo $SENSOR_AS726 | cut -f12 -d" "`
SENSOR_AS726_ORANGE=`echo $SENSOR_AS726 | cut -f14 -d" "`
SENSOR_AS726_RED=`echo $SENSOR_AS726 | cut -f16 -d" "`

curl "https://api.thingspeak.com/update?api_key=1S77WR1PA1ICK9QN&field1=$SENSOR_AS726_VIOLET&field2=$SENSOR_AS726_BLUE&field3=$SENSOR_AS726_GREEN&field4=$SENSOR_AS726_YELLOW&field5=$SENSOR_AS726_ORANGE&field6=$SENSOR_AS726_RED"


SENSOR_TSL2591_DATA=`echo $SENSOR_TSL2591 | cut -f8 -d" "`
SENSOR_LPS35HW_PRESS=`echo $SENSOR_LPS35HW | cut -f6 -d" "`
SENSOR_LPS35HW_TEMP=`echo $SENSOR_LPS35HW | cut -f9 -d" "`

SENSOR_SGP30_ECO2=`echo $SENSOR_SGP30 | cut -f4 -d" "`
SENSOR_SGP30_TVOC=`echo $SENSOR_SGP30 | cut -f8 -d" "`

SENSOR_MCP9808_TEMP=`echo $SENSOR_MCP9808 | cut -f3 -d" "`

SENSOR_BME280_HUM=`echo $SENSOR_BME280 | cut -f6 -d" "`
SENSOR_BME280_PRESS=`echo $SENSOR_BME280 | cut -f9 -d" "`
curl "https://api.thingspeak.com/update?api_key=45CA3NOPOX05JFWX&field1=$SENSOR_TSL2591_DATA&field2=$SENSOR_LPS35HW_PRESS&field3=$SENSOR_LPS35HW_TEMP&field4=$SENSOR_SGP30_ECO2&field5=$SENSOR_SGP30_TVOC&field6=$SENSOR_MCP9808_TEMP&field7=$SENSOR_BME280_HUM&field8=$SENSOR_BME280_PRESS"

