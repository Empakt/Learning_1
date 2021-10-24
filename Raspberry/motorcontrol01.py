from gpiozero import PWMLED
from time import sleep

motorF = PWMLED(2)
motorB = PWMLED(3)
motorValue = 0
minMaxSpeedTime = 1
goingDown = False
smoothTransitionValue = 0.02
smoothTransitionSleep = 0.05

while True:
	motorF.value = 1
	motorB.value = 0
	sleep(minMaxSpeedTime)
	goingDown = True

	while motorF.value > 0 and goingDown:
		motorValue = motorF.value - smoothTransitionValue
		if motorValue < 0:
			motorValue = 0
		motorF.value = motorValue
		sleep(smoothTransitionSleep)
		if motorF.value <= 0:
			goingDown = False

	while motorF.value <= 0 and not goingDown:
		motorValue = motorB.value + smoothTransitionValue
		if motorValue > 1:
			motorValue = 1
		motorB.value = motorValue
		sleep(smoothTransitionSleep)
		if motorB.value >= 1:
			goingDown = True

	motorF.value = 0
	motorB.value = 1
	sleep(minMaxSpeedTime)
	goingDown = False

	while motorB.value > 0 and not goingDown:
		motorValue = motorB.value - smoothTransitionValue
		if motorValue < 0:
			motorValue = 0
		motorB.value = motorValue
		sleep(smoothTransitionSleep)
		if motorB.value <= 0:
			goingDown = True

	while motorB.value <= 0 and goingDown:
		motorValue = motorF.value + smoothTransitionValue
		if motorValue > 1:
			motorValue = 1
		motorF.value = motorValue
		sleep(smoothTransitionSleep)
		if motorF.value >= 1:
			goingDown = False
