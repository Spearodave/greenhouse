import time
import sys

import Adafruit_DHT
import RPi.GPIO as GPIO

def readAdafruitDHT(moduleType,pin):
    """returns the humidity and temperature as integers."""
    sensor_args = { '11': Adafruit_DHT.DHT11,
                '22': Adafruit_DHT.DHT22,
                '2302': Adafruit_DHT.AM2302 }
    sensor = sensor_args[moduleType]

    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    return (int(humidity), int(temperature))
    

if __name__ == '__main__':
    #Setup the GPIO 
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(18,GPIO.OUT)
    
    try:
        while True:
            # Read the temperature and humidity
            humidity, temperature = readAdafruitDHT('11',4)
            # If the temp is > 30 turn the pin on
            if temperature >20:
                GPIO.output(18,GPIO.HIGH)
            else:
                GPIO.output(18,GPIO.LOW)
            time.sleep(60)
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("Bye")

