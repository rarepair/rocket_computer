import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)

sleep(10) #Plus 5 + 5

while True: # Run forever
 GPIO.output(16, GPIO.HIGH)
 #print("High ")
 sleep(0.4) # Sleep for 1 second
 GPIO.output(16, GPIO.LOW)
 #print("Low ")
 sleep(0.4) # Sleep for 1 second
