from gpiozero import LED, Button

button1 = Button(2)
button2 = Button(3)
led = LED(4)

while True:
	if button1.is_pressed:
		led.on()
	if button2.is_pressed:
		led.off()
