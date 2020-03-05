from pynput.mouse import Button, Controller
import webbrowser
import time
import random

mouse = Controller()

time.sleep(1)


# mouse.position = (1040, 320)
# mouse.click(Button.left, 1)

# time.sleep(1)

for i in range(5):
	#opens vials
	mouse.position = (1013, 244)
	mouse.click(Button.right, 1)
	time.sleep(3 + .0001 * random.randrange(1, 500))


	#selects vials
	mouse.position = (1010, 345)
	time.sleep(2 + .0001 * random.randrange(1, 500))
	mouse.click(Button.left, 1)
	time.sleep(2 + .0001 * random.randrange(1, 500))


	#close bank
	mouse.position = (1170, 93)
	time.sleep(2 + .0001 * random.randrange(1, 500))
	mouse.click(Button.left, 1)
	time.sleep(10 + .0001 * random.randrange(1, 500))


	#select vials in inv
	mouse.position = (1270, 251)
	time.sleep(2 + .0001 * random.randrange(1, 500))
	mouse.click(Button.left, 1)
	time.sleep(2 + .0001 * random.randrange(1, 500))

	#click on fountain
	mouse.position = (1050, 430)
	time.sleep(2 + .0001 * random.randrange(1, 500))
	mouse.click(Button.left, 1)
	time.sleep(20 + .0001 * random.randrange(1, 500))

	for i in range(random.randrange(1, 10)):
		x = random.randrange(1240, 1426)
		y = random.randrange(240, 490)
		time.sleep(2 + .0001 * random.randrange(1, 500))
		mouse.position = (x, y)
		time.sleep(2 + .0001 * random.randrange(1, 500))
		mouse.click(Button.left, 1)	


	#click the bank
	mouse.position = (1039, 257)
	time.sleep(2 + .0001 * random.randrange(1, 500))
	mouse.click(Button.left, 2)
	mouse.click(Button.left, 1)
	time.sleep(5 + .001 * random.randrange(1, 500))

	#empty pouch
	mouse.position = (1125, 385)
	time.sleep(2 + .0001 * random.randrange(1, 500))
	mouse.click(Button.left, 2)
	time.sleep(2 + .0001 * random.randrange(1, 500))


	

