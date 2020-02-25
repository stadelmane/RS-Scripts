from pynput.mouse import Button, Controller
import webbrowser
import time
import random

mouse = Controller()

timeRunning = 0

while True:
	for i in range(random.randrange(1, 3)):
		x = random.randrange(800, 925)
		y = random.randrange(160, 255)
		time.sleep(2 + .0001 * random.randrange(1, 500))
		mouse.position = (x, y)
		time.sleep(2 + .0001 * random.randrange(1, 500))
		mouse.click(Button.left, 1)	
		print("clicked at " , timeRunning)
	timeToSleep = random.randrange(30, 150)
	time.sleep(int(timeToSleep))
	timeRunning += timeToSleep


	

