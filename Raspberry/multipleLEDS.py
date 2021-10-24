from gpiozero import LED
from time import sleep

led1 = LED(2)
led2 = LED(3)
led3 = LED(4)
led4 = LED(17)
led5 = LED(27)

while True:
	led1.on()
	led2.on()
	led3.on()
	led4.on()
	led5.on()
	sleep(0.1)
	led1.off()
	led2.off()
	led3.off()
	led4.off()
	led5.off()
	sleep(0.1)
