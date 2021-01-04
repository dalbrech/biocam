import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

print("testing DHT22")

if True:
   humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

   if humidity is not None and temperature is not None:
      print("Temp:   {0:0.1f}'C  Hum: {1:0.1f}".format(temperature, humidity))
   else:
      print("No temp / RH reading")

