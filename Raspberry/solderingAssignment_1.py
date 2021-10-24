from gpiozero import LED, Button
import time

button1 = Button(6)
button2 = Button(13)
buttonLed1 = LED(19)
buttonLed2 = LED(26)

segments = [LED(2), LED(3), LED(4), LED(17), LED(18), LED(27), LED(22)]

sleepDuration = 0.3
sleepTime = 0
button1Again = True
button2Again = True

currentNumber = 0

for i in range(7):
	segments[i].on()
segments[6].off()

while True:
	#print(currentNumber)
	if button1.is_pressed and time.time() > sleepTime + sleepDuration: #button1Again
		buttonLed1.on()
		button1Again = False
		sleepTime = time.time()

		for i in range(7):
			segments[i].off()

		if currentNumber == 9:
			for i in range(7):
				segments[i].on()
			segments[6].off()
			currentNumber = 0
			button1Again = True
		if currentNumber == 8:
			for i in range(7):
				segments[i].on()
			segments[5].off()
			currentNumber = 9
		if currentNumber == 7:
			for i in range(7):
				segments[i].on()
			currentNumber = 8
		if currentNumber == 6:
			segments[1].on()
			segments[2].on()
			segments[3].on()
			currentNumber = 7
		if currentNumber == 5:
			segments[0].on()
			segments[1].on()
			segments[3].on()
			segments[4].on()
			segments[5].on()
			segments[6].on()
			currentNumber = 6
		if currentNumber == 4:
			segments[0].on()
			segments[1].on()
			segments[3].on()
			segments[4].on()
			segments[6].on()
			currentNumber = 5
		if currentNumber == 3:
			segments[0].on()
			segments[2].on()
			segments[3].on()
			segments[6].on()
			currentNumber = 4
		if currentNumber == 2:
			segments[1].on()
			segments[2].on()
			segments[3].on()
			segments[4].on()
			segments[6].on()
			currentNumber = 3
		if currentNumber == 1:
			segments[1].on()
			segments[2].on()
			segments[4].on()
			segments[5].on()
			segments[6].on()
			currentNumber = 2
		if currentNumber == 0 and not button1Again:
			segments[2].on()
			segments[3].on()
			currentNumber = 1

	if not button1.is_pressed:
		buttonLed1.off()
		#button1Again = True

	if button2.is_pressed and time.time() > sleepTime + sleepDuration: #button2Again
		buttonLed2.on()
		button2Again = False
		sleepTime = time.time()

		for i in range(7):
			segments[i].off()

		if currentNumber == 1:
			for i in range(7):
				segments[i].on()
			segments[6].off()
			currentNumber = 0
			button2Again = True
		if currentNumber == 2:
			segments[2].on()
			segments[3].on()
			currentNumber = 1
		if currentNumber == 3:
			segments[1].on()
			segments[2].on()
			segments[4].on()
			segments[5].on()
			segments[6].on()
			currentNumber = 2
		if currentNumber == 4:
			segments[1].on()
			segments[2].on()
			segments[3].on()
			segments[4].on()
			segments[6].on()
			currentNumber = 3
		if currentNumber == 5:
			segments[0].on()
			segments[2].on()
			segments[3].on()
			segments[6].on()
			currentNumber = 4
		if currentNumber == 6:
			segments[0].on()
			segments[1].on()
			segments[3].on()
			segments[4].on()
			segments[6].on()
			currentNumber = 5
		if currentNumber == 7:
			segments[0].on()
			segments[1].on()
			segments[3].on()
			segments[4].on()
			segments[5].on()
			segments[6].on()
			currentNumber = 6
		if currentNumber == 8:
			segments[1].on()
			segments[2].on()
			segments[3].on()
			currentNumber = 7
		if currentNumber == 9:
			for i in range(7):
				segments[i].on()
			currentNumber = 8
		if currentNumber == 0 and not button2Again:
			for i in range(7):
				segments[i].on()
			segments[5].off()
			currentNumber = 9

	if not button2.is_pressed:
		buttonLed2.off()
		#button2Again = True

	"""if time.time() > sleepTime + sleepDuration:
		if currentNumber == 0:
			for i in range(7):
				segments[i].on()
			currentNumber = 8
		else:
			for i in range(7):
				segments[i].off()
			currentNumber = 0

		sleepTime = time.time()"""

	#print("%f" % time.time())
	#print(time.time())
