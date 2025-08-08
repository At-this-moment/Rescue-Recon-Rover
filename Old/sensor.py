import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN)
try:
 while True:
  if GPIO.input(24):
   print ("0")
  else:
   print ("1")
except KeyboardInterrupt:
 print ("!!!!!!!")
 GPIO.cleanup()