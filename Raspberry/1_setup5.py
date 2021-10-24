from gpiozero import Button
from time import sleep

b1 = Button(2)
b2 = Button(3)
b3 = Button(17)
b4 = Button(27)

failedPin = False
count = 0
buttonDelay = 0.5

while True:
	failedPin = False
	count = 0
	print("Starting from beginning")

	while not failedPin:
		if b1.is_pressed:
			if count == 1:
				count = 2
			else:
				failedPin = True
				#print("Wrong PIN, restarting")
			sleep(buttonDelay)
		if b2.is_pressed:
			if count == 3:
				count = 4
			else:
				failedPin = True
				#print("Wrong PIN, restarting")
			sleep(buttonDelay)
		if b3.is_pressed:
			if count == 0:
				count = 1
			else:
				failedPin = True
				#print("Wrong PIN, restarting")
			sleep(buttonDelay)
		if b4.is_pressed:
			if count == 2:
				count = 3
			else:
				failedPin = True
				#print("Wrong PIN, restarting")
			sleep(buttonDelay)
		if count == 4:
			print("Entered correct PIN, door unlocked")
			failedPin = True
			sleep(buttonDelay)
		sleep(0.01)
