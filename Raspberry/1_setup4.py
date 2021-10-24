from gpiozero import LED, Button
from time import sleep

button1 = Button(2)
button2 = Button(3)
button3 = Button(17)
button4 = Button(27)

count = 0

while True:
	if button1.is_pressed and count == 0:
		count = 1
	if button2.is_pressed and count == 1:
		count = 2
	if button3.is_pressed and count == 2:
		count = 3
	if button4.is_pressed:
		count = 0

	print(count)
	sleep(0.1)
