""" Example for using the SGP30 with CircuitPython and the Adafruit library"""

import time
import board
import busio
import adafruit_sgp30

i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)

# Create library object on our I2C port
sgp30 = adafruit_sgp30.Adafruit_SGP30(i2c)

#print("SGP30 serial number", [hex(i) for i in sgp30.serial])

sgp30.iaq_init()
sgp30.set_iaq_baseline(0x8973, 0x8AAE)

elapsed_sec = 0
co2=sgp30.eCO2
tvoc=sgp30.TVOC
while elapsed_sec < 30:
	time.sleep(1)
	co2=sgp30.eCO2
	tvoc=sgp30.TVOC
	elapsed_sec+=1 
print("SGP30 eCO2 = {0:0.1f} ppm TVOC = {1:0.1f} ppb".format(sgp30.eCO2, sgp30.TVOC))


