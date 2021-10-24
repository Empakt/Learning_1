from gpiozero import LED
from time import sleep

green = LED(2)
yellow = LED(3)
red = LED(4)

while True:
	green.on()
	sleep(2)
	green.off()
	yellow.on()
	sleep(2)
	yellow.off()
	red.on()
	sleep(2)
	yellow.on()
	sleep(2)
	yellow.off()
	red.off()
