from RPi import GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

LEDS = (5,12,16,6,13,17)

GPIO.setup(LEDS, GPIO.OUT, initial=0)

try:
        i = 0
        led_length = len(LEDS)
        while i < led_length:
                if i == 0:
                        GPIO.output(LEDS[led_length-1],0)
                else:
                        GPIO.output(LEDS[i-1],0)
                GPIO.output(LEDS[i],1)
                i += 1
                if i == led_length:
                        i = 0
                sleep(.2)
except:
        GPIO.cleanup()
