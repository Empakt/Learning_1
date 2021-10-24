from gpiozero import LED
from time import sleep

myLed = LED(3)

while True:
	myLed.on()
	sleep(0.1)
	myLed.off()
	sleep(0.1)
