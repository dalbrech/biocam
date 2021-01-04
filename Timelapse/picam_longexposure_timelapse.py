"""
The following is PiCamera-based timelapse code.
Created by:Sam Hopkins
Advised by: Dirk Albrecht
Last Updated: 8/15/2020

The goal of this program is to take timelapses as determined by user 
input from Motioneye. It uses a few sensors, 
that can be commented out as necessary.
It will also turn the timelapse of images into short videos at the end.

"""

from picamera import PiCamera
from picamera import Color
from time import sleep
from fractions import Fraction
from datetime import datetime
import time
import board
import busio
#TSL12591 light sensor
import adafruit_tsl2591
#LPS35HW temperature and pressure
import adafruit_lps35hw
#BME280 temperature, pressure, and humidity
import adafruit_bme280
#SGP30 gas sensor
import adafruit_sgp30
#for making timelapse
import subprocess
#import io
import shutil



#for testing speeds
def how_long(start, op):
    print('%s took %.2fs' % (op, time.time() - start))
    return time.time()


#get camera shutter
camera_shutter=open("/etc/motioneye/camera-2.shutter", "r")
shutter_speed=float(camera_shutter.readline())
camera_shutter.close()
#print(shutter_speed)

#get timelapse duration in seconds
timelapse_duration=open("/etc/motioneye/camera-2.tlduration","r")
timelapse_hours=float(timelapse_duration.readline())
#print(timelapse_hours)
timelapse_seconds =timelapse_hours*60*60
#print(timelapse_seconds)
timelapse_duration.close()
# Set a framerate of 1/6fps, then set shutter
# speed to 6s and ISO to 800, text size to 80
#2592x1944
#1280 x 720
#2048x1152 max ffmpeg can handle, Picam can go to 2592x 1944
camera = PiCamera(resolution=(2592, 1152), framerate=(1/shutter_speed)) 
camera.shutter_speed = int(1000000 * shutter_speed)
camera.iso = 800
camera.annotate_text_size=80
camera.annotate_background=Color(y=0.0,u=0.0,v=0.0)
# Give the camera a good long time to set gains and
# measure AWB (you may wish to use fixed AWB instead)
sleep(30)
camera.exposure_mode = 'off'




# Initialize the I2C bus.
i2c = busio.I2C(board.SCL, board.SDA)


# Initialize the TSL2591sensor, light, total and IR
tsl = adafruit_tsl2591.TSL2591(i2c)
#Initialize LPS35HW, temp, pressure
lps = adafruit_lps35hw.LPS35HW(i2c)
#Initialize BME280, temp, pressure, humidity
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)
# change this to match the location's pressure (hPa) at sea level
bme280.sea_level_pressure = 1013.25
#Initialize SGP30.py, equivalent carbon and total volatile organic carbon
#sgp30 = adafruit_sgp30.Adafruit_SGP30(i2c)
#sensor is indirect carbon sensor, needs algorithm
#initialize algorithm
#sgp30.iaq_init()
# and also needs baselines
#sgp30.set_iaq_baseline(0x8973, 0x8AAE)

"""
#let gas sensor run for 30 seconds warmup/get good data
elapsed_sec = 0

co2=sgp30.eCO2
print(co2)
tvoc=sgp30.TVOC
print(tvoc)
while elapsed_sec < 30:
	time.sleep(1)
	co2=sgp30.eCO2
	print(co2)
	tvoc=sgp30.TVOC
	print(tvoc)
	elapsed_sec+=1
"""
#initialize variables
now=""
a=0
frame_numbers=100
start=time.time()
print(start)
#set text size
camera.annotate_text_size=50



#get start and date time to name files
date_name=datetime.now().strftime("%Y_%m_%d_%H_%M_%S_%f")
#make a new folder for images
directory='/var/lib/motioneye/Camera1/'
#directory='/home/pi/MicroscopeImages/'
subprocess.call('sudo mkdir ' + directory + date_name, shell=True)


#make parallel webpage to display the latest image
#go to your.ip.address:8765/static/last_image.jpg to view latest image
#go to your.ip.address:8765/static/timelapse.avi to view the latest timelapse video
subprocess.call('sudo python3 /home/pi/Timelapse/page.py 8765 &', shell = True)




#for saving images with timestamps (ffmpeg will not work)
#for filename in camera.capture_continuous("/home/pi/MicroscopeImages/{timestamp:%Y_%m_%d_%H_%M_%S_%f}.jpg", use_video_port=True):

time_now=time.time()

#take images until time is up, annotate them with sensor data, save them to the new folder
test=time.time()
for filename in camera.capture_continuous(directory  + date_name +"/image{counter:07}.jpg", use_video_port=True):
	print(filename)
	shutil.copyfile(filename, '/home/pi/Timelapse/static/last_image.jpg')
	now=datetime.now()
	date_time=now.strftime("%Y_%m_%d_%H_%M_%S_%f")
	#print(date_time)
	a=a+1
	#how_long(time_now,"copying and names")
	#show speed betwen each image
	print((time.time()-test))
	test=time.time()
	#precise sensor checking
	"""try:
		lux = tsl.lux #get light
		#print("Lux PASSED")
	except:
		lux= -1000
		#print("Lux FAILED")
	try:
		infrared = tsl.infrared #get infrared light
		#print("IR PASSED")
	except:
		infrared = -1000
		#print("IR FAILED")
	try:
		pressure=lps.pressure  #get pressure
		#print("Pressure PASSED")
	except:
		pressure= -1000
		#print("Pressure FAILED")
	try:
		temperature=lps.temperature #get temperature
		#print("Temp PASSED")
	except:
		temperature=-1000
		#print("Temp FAILED")
	try:
		humidity=bme280.humidity  #get humidty
		#print("Humidity PASSED")
	except:
		humidity=-1000
		#print("Humidity FAILED")
	#try:
	#	eco2=sgp30.eCO2	#get equivalent carbon 
		#print("CO PASSED")
	#except:
	eco2=-1000
		#print("CO FAILED")
	#try:
	#	tvoc=sgp30.TVOC    # get total volatile organic compounds
		#print("TVOC PASSED")
	#except:
	tvoc=-1000
		#print("TVOC FAILED")
	"""
	#pooled sensor checking (to save time)
	try:
		lux = tsl.lux #get light
#		how_long(time_now, "lux")
		infrared = tsl.infrared #get infrared light
#		how_long(time_now,"IR")
		pressure=lps.pressure  #get pressure
#		how_long(time_now,"Pressure")
		temperature=lps.temperature #get temperature
#		how_long(time_now,"Temp")
		humidity=bme280.humidity  #get humidity
#		how_long(time_now, "Humidity")
#		eco2=sgp30.eCO2	#get equivalent carbon
		eco2=-1000
		tvoc=eco2
#		how_long(time_now,"eCO2")
#		tvoc=sgp30.TVOC    # get total volatile organic compounds
#		how_long(time_now,"TVOC")
	except:
		lux= -1000
		infrared = -1000
		pressure= -1000
		temperature=-1000
		humidity=-1000
		eco2=-1000
		tvoc=-1000

	#how_long(time_now,"sensors")
	#print on image, date, light, IR light, pressure and temp
	camera.annotate_text= date_time + " TL: {0:0.001f} IR: {1} Pres {2:0.1f} hPa Temp {3:0.1f} C Hum {4:0.1f} % eCO2 {5:0.1f} ppm TVOC {6:0.1f} ppb".format(lux,infrared,pressure,temperature,humidity,eco2,tvoc) +  " Frame: "  + str(a)	 + " Time {0:0.3f}".format(time.time() -start) 
	#just print frame # and time
	#camera.annotate_text= " Frame: "  + str(a) + " Time {0:0.3f}".format(time.time() -start)
	#make a timelapse every frame_number images during timelapse (slows
	#down process, requires lot of power to do
	#if (a % frame_numbers) == 0:
		#subprocess.Popen('sudo ffmpeg -start_number ' + str(a-frame_numbers) + ' -r 10 -i '+ directory + date_name +'/image%07d.jpg -frames:v ' + str(frame_numbers) + ' -r 10 -vcodec libx264 -preset faster -crf 20 -g 15 '+ directory + date_name + '/timelapse' + str(a) + date_name + '.avi', shell=True)
	#if a>=220:   #run for a set number of frames
	#time.sleep(10) #if you want to delay images, but keep exposure time
	if (time.time() - start) > timelapse_seconds:
		break
	#how_long(time_now, "overlay")


#set camera framerate back to 1 to avoid hanging, 
#close camera
camera.framerate=1
camera.close()




#make timelapse videos out of images, every 100 images
for i in range(1, 1+(a//frame_numbers)):
	b=i*frame_numbers
	subprocess.call('sudo ffmpeg -start_number ' + str(b-frame_numbers) + ' -r 10 -i '+ directory + date_name +'/image%07d.jpg -frames:v ' + str(frame_numbers) + ' -r 10 -vcodec libx264 -preset faster -crf 20 -g 15 '+ directory + date_name + '/timelapse' + str(b) + date_name + '.avi', shell=True)
	shutil.copyfile(directory + date_name + '/timelapse' + str(b) + date_name + '.avi', '/home/pi/Timelapse/static/timelapse.avi')
#make a complete timelapse at the end, only if your pi has enough power to do so
#subprocess.call('sudo ffmpeg -r 10 -i ' +directory + date_name + '/ image%07d.jpg -r 10 -vcodec libx264 -crf 20 -g 15 '+ directory + date_name + '/timelapse.avi', shell=True)

#kill webpage so motioneye can start.
# !!! program killed elsewhere, legacy method left in
#subprocess.call('sudo pkill -f page.py', shell = True)


print("Done!")

