import time
 
import board
import busio
 
 
#MPRLS
import adafruit_mprls
 
 
# Initialize the I2C bus.
i2c = busio.I2C(board.SCL, board.SDA)
 
 
 
 
#Initialize MPRLS
#connect to default over I2C
mpr = adafruit_mprls.MPRLS(i2c, psi_min=0, psi_max=25)
 
# You can also specify both reset and eoc pins
"""
import digitalio
reset = digitalio.DigitalInOut(board.D5)
eoc = digitalio.DigitalInOut(board.D6)
mpr = adafruit_mprls.MPRLS(i2c, eoc_pin=eoc, reset_pin=reset,
                           psi_min=0, psi_max=25)
"""
 
#Simple Demo of MPRLS
#print("\n")
#print("MPRLS -Ported Pressure-")
print("MPRLS Pressure (hPa): {0:0.1f}".format(mpr.pressure))

