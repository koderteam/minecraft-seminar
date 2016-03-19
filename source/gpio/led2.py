import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)


GPIO.output(21, GPIO.LOW)
print("LED is on")
GPIO.output(21, GPIO.HIGH)
time.sleep(10)
print("LED is off")
GPIO.output(21, GPIO.LOW)
