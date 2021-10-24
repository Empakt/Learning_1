from gpiozero import PWMLED
from time import sleep

led = PWMLED(4)
upToDown = True
brightness = 0

while True:
	if upToDown:
		brightness += 0.01
	else:
		brightness -= 0.01

	if brightness > 1:
		brightness = 1
		upToDown = False
	if brightness < 0:
		brightness = 0
		upToDown = True

	led.value = brightness

	sleep(0.01)

	"""led.value = 0.3
	sleep(1)
	led.value = 0.6
	sleep(1)
	led.value = 1
	sleep(1)"""
