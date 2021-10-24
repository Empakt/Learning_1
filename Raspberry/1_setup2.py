from gpiozero import LED, Button

button1 = Button(2)
button2 = Button(3)
button3 = Button(17)
button4 = Button(27)

led1 = LED(4)
led2 = LED(22)

while True:
	if button1.is_pressed:
		led1.on()
	if button2.is_pressed:
		led1.off()
	if button3.is_pressed:
		led2.on()
	if button4.is_pressed:
		led2.off()

