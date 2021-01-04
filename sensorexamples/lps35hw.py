import time
 
import board
import busio




#LPS35HW
import adafruit_lps35hw


 
# Initialize the I2C bus.
i2c = busio.I2C(board.SCL, board.SDA)


#Initialize LPS35HW
lps = adafruit_lps35hw.LPS35HW(i2c)


#Simple Demo of LPS35HW (Water Resistant Pressure)
#print("\n")
#print("LPS35HW -Water Resistant Pressure-")
#print("Pressure: %.2f hPa" % lps.pressure)
#print("Temperature: %.2f C" % lps.temperature)
#print("")


print("LPS35HW -Water Resistant Pressure- Pressure: {0:0.1f} hPa Temperature: {1:0.1f} C".format(lps.pressure,lps.temperature))
#print("Pressure: %.2f hPa" % lps.pressure)
#print("Temperature: %.2f C" % lps.temperature)

