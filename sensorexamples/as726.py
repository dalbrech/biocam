import time
import board
import busio
 
#AS726x_I2C
from adafruit_as726x import AS726x_I2C
 
# Initialize the I2C bus.
i2c = busio.I2C(board.SCL, board.SDA)
 
#Initialize the AS726x Sensor
sensor_as726 = AS726x_I2C(i2c)
#continuously gather samples of all colors
sensor_as726.conversion_mode = sensor_as726.MODE_2
 
#Simple demo of AS726x Sensor
    #wait for data to be ready
while not sensor_as726.data_ready:
  time.sleep(0.1) 
    	
    #print color values
#print("\n")
#print("AS726x -6 Color Light-")
#print("V: ", sensor_as726.violet)
#print("B: ",sensor_as726.blue)
#print("G: ",sensor_as726.green)
#print("Y: ",sensor_as726.yellow)
#print("O: ",sensor_as726.orange)
#print("R: ",sensor_as726.red)
 
print("AS726x -6 Color Light- V: {0:0.1f} B: {1:0.1f} G: {2:0.1f} Y: {3:0.1f} O: {4:0.1f} R: {5:0.1f}".format(sensor_as726.violet, sensor_as726.blue, sensor_as726.green, sensor_as726.yellow, sensor_as726.orange, sensor_as726.red))      

