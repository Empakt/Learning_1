from gpiozero import LED, Button

button1 = Button(2)
button2 = Button(3)

led1 = LED(4)
led2 = LED(22)
led3 = LED(18)
led4 = LED(23)

while True:
	if button1.is_pressed and button2.is_pressed:
		led1.on()
	else:
		led1.off()
	if button1.is_pressed or button2.is_pressed:
		led2.on()
	else:
		led2.off()
	if not button1.is_pressed:
		led3.on()
	else:
		led3.off()
	"""if (button1.is_pressed and not button2.is_pressed) or (not button1.is_pressed and button2.is_pressed):
		led4.on()
	else:
		led4.off()"""
	if button1.is_pressed ^ button2.is_pressed:
		led4.on()
	else:
		led4.off()
