import RPi.GPIO as GPIO
import time
LED = 0
RELAYS = [16, 18, 20, 21, 23, 24]
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
for LED in RELAYS:
    GPIO.setup(LED,GPIO.OUT)
    print "LED on"
    GPIO.output(LED,GPIO.HIGH)
    time.sleep(5)
    print "LED off"
    GPIO.output(LED,GPIO.LOW)
