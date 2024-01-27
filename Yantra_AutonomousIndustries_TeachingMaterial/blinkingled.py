#blink with RPi.GPIO library and by setting mode as BCM.
# BCM -- Broadcom chip-specific pin numbers 
#hey frime the ram rma
import RPi.GPIO as GPIO
import time
ledPin = 23
GPIO.setmode(GPIO.BCM )
GPIO.setwarnings(False) # to stop the warnings
GPIO.setup(ledPin,GPIO.OUT) # setting the led pin to output

while True:
    GPIO.output(ledPin, GPIO.HIGH)
    print('LED ON')
    time.sleep(1)
    GPIO.output(ledPin, GPIO.LOW)
    print('LED OFF')
    time.sleep(1)