from gpiozero import LED, Button
#from signal import pause

led = LED(4)
button1 = Button(2)
button2 = Button(3)

#button1.when_pressed = led.on
#button1.when_released = led.off

#pause()

while True:
	if button1.is_pressed and button2.is_pressed:
		led.on()
		#print("Buttons are pressed")
	else:
		led.off()
		#print("Buttons are not pressed")
