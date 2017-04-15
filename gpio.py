import os
import time
import RPi.GPIO as GPIO

#setup GPIO using Board numbering
GPIO.setmode(GPIO.BCM)


def testGPIO(pin):
	if GPIO.input(pin):
		print('%i Input was HIGH' % pin)
	else:
		print('%i Input was LOW' % pin)

def setupGPIO(pin):
	GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)



for pin in range(0,40):
	setupGPIO(pin)

while True:
	os.system('clear')
	for pin in range(0,40):
		testGPIO(pin)
	time.sleep(1)
GPIO.cleanup()
