import time

import board
import busio
import adafruit_bme280

# Create library object using our Bus I2C port
i2c = busio.I2C(board.SCL, board.SDA)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

# OR create library object using our Bus SPI port
# spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
# bme_cs = digitalio.DigitalInOut(board.D10)
# bme280 = adafruit_bme280.Adafruit_BME280_SPI(spi, bme_cs)

# change this to match the location's pressure (hPa) at sea level
bme280.sea_level_pressure = 1013.25

print("BME280 Temperature: {0:0.1f} C Humidity: {1:0.1f} Per.  Pressure {2:0.1f} hPa Altitude {3:0.2f} meters".format(bme280.temperature, bme280.humidity,bme280.pressure,bme280.altitude))


#    print("Humidity: %0.1f %%" % bme280.humidity)
 #   print("Pressure: %0.1f hPa" % bme280.pressure)
  #  print("Altitude = %0.2f meters" % bme280.altitude)
   # time.sleep(2)
