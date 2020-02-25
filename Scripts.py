from pynput.mouse import Button, Controller
import webbrowser
import time
import random
import pyautogui


def moveLeft():
	mouse = Controller()
	for over in range(4):
		for down in range(2):
			mouse.position = (667, 345)
			time.sleep(1 + .0001 * random.randrange(1, 500))
			mouse.click(Button.left, 1)



def lightLogs():
	mouse = Controller()
	for over in range(4):
		for down in range(1):
			mouse.position = (1005, 260)
			time.sleep(1 + .0001 * random.randrange(1, 500))
			mouse.click(Button.left, 1)

			mouse.position = (1008 + 41 * over , 294 + 37 * down)
			time.sleep(1 + .0001 * random.randrange(1, 500))
			mouse.click(Button.left, 1)	
			time.sleep(10 + .0001 * random.randrange(1, 500))
	moveLeft()

def logOut():
	mouse = Controller()
	x , y = random.randrange(1147, 1165) , random.randrange(74, 92)
	pyautogui.moveTo(x, y, duration = (.3 + .01 * random.randrange(1, 5)))
	mouse.click(Button.left, 1)
	x , y = random.randrange(1005, 1130) , random.randrange(450, 470)
	pyautogui.moveTo(x, y, duration = (.3 + .01 * random.randrange(1, 5)))
	mouse.click(Button.left, 1)



def dropLogs():
	mouse = Controller()
	for over in range(4):
		for down in range(6):
			x , y = droppos(1005 + 40 * over , 295 + 33 * down)
			# mouse.position = (x , y)
			pyautogui.moveTo(x, y, duration = (.2 + .01 * random.randrange(1, 5)))
			# mouse.position = (1008 + 41 * over , 294 + 37 * down)
			# time.sleep(.35 + .0001 * random.randrange(1, 500))
			mouse.click(Button.left, 1)	

def mineEss():
	for i in range(100):
		mouse = Controller()
		x , y = Esspos(729, 236)
		pyautogui.moveTo(x, y, duration = (.75 + .01 * random.randrange(1, 5)))
		time.sleep(1 + .0001 * random.randrange(1, 500))
		mouse.click(Button.left, 1)
		im = pyautogui.screenshot()
		count = 0
		while (pyautogui.pixelMatchesColor(1133, 473, (67, 61, 61), tolerance = 0) != True):
			time.sleep(.001 * random.randrange(1, 500))
			count += 1
			im = pyautogui.screenshot()
			if count > 120:
				count = 0
				x , y = Esspos(729, 236)
				pyautogui.moveTo(x, y, duration = (.01 * random.randrange(10, 25)))
				time.sleep(1 + .0001 * random.randrange(1, 500))
				mouse.click(Button.left, 1)
		print(count)
		dropLogs()

def droppos(x , y):
	x = random.randrange(x, x + 10)
	y = random.randrange(y, y + 10)
	return (x , y)

def Esspos(x , y):
	x = random.randrange(x, x + 50)
	y = random.randrange(y, y + 50)
	return (x , y)

def coalpos(x , y):
	x = random.randrange(x, x + 50)
	y = random.randrange(y, y + 50)
	return (x , y)

def minecoal():
	failures = 0
	mouse = Controller()
	# while(1):
	for j in range(1):
		for i in range(2):
			failures = 0

			im = pyautogui.screenshot()
			if pyautogui.pixelMatchesColor(752, 500, (39, 20, 14), tolerance =20):
				x , y = coalpos(729 , 428)
				mouse.position = (x, y)
				time.sleep(.1 + .0001 * random.randrange(1, 500))
				mouse.click(Button.left, 2)
				while(pyautogui.pixelMatchesColor(752, 500, (39, 20, 14), tolerance =20)):
					failures += 1
					im = pyautogui.screenshot()
					if failures % 6 == 0:
						mouse.click(Button.left, 1)

			failures = 0

			if pyautogui.pixelMatchesColor(675, 330, (50, 26, 17), tolerance =20):
				x , y = coalpos(620 , 310)
				mouse.position = (x, y)
				time.sleep(.1 + .0001 * random.randrange(1, 500))
				mouse.click(Button.left, 2)
				while(pyautogui.pixelMatchesColor(675, 330, (50, 26, 17), tolerance = 20)):
					failures += 1
					im = pyautogui.screenshot()
					if failures % 6 == 0:
						mouse.click(Button.left, 1)

			failures = 0

			if pyautogui.pixelMatchesColor(750, 275, (57, 30, 20), tolerance =20):
				x , y = coalpos(735 , 205)
				mouse.position = (x, y)
				time.sleep(.1 + .0001 * random.randrange(1, 500))
				mouse.click(Button.left, 2)
				while(pyautogui.pixelMatchesColor(750, 275, (57, 30, 20), tolerance = 15)):
					im = pyautogui.screenshot()
					failures += 1
					if failures % 6 == 0:
						mouse.click(Button.left, 1)

		# dropLogs()

def fastminecoal():
	failures = 0
	mouse = Controller()
	# while(1):
	for j in range(1000):
		for i in range(8):
			x , y = coalpos(729 , 435)
			mouse.position = (x, y)
			time.sleep(.5 + .0001 * random.randrange(1, 500))
			mouse.click(Button.left, 2)
			time.sleep(2 + .0001 * random.randrange(1, 500))

			x , y = coalpos(620 , 320)
			mouse.position = (x, y)
			time.sleep(.5 + .0001 * random.randrange(1, 500))
			mouse.click(Button.left, 2)
			time.sleep(2 + .0001 * random.randrange(1, 500))

			x , y = coalpos(735 , 215)
			mouse.position = (x, y)
			time.sleep(.5 + .0001 * random.randrange(1, 500))
			mouse.click(Button.left, 2)
			time.sleep(2 + .0001 * random.randrange(1, 500))

		dropLogs()
		time.sleep(random.randrange(1, 7) + .0001 * random.randrange(1, 500))

		


def minecoaldumb():
	mouse = Controller()
	time.sleep(3 + .0001 * random.randrange(1, 500))
	mouse.position = (785, 351)
	time.sleep(2 + .0001 * random.randrange(1, 500))
	mouse.click(Button.left, 1)

	mouse = Controller()
	time.sleep(4 + .0001 * random.randrange(1, 500))
	mouse.position = (746, 325)
	time.sleep(2 + .0001 * random.randrange(1, 500))
	mouse.click(Button.left, 1)

	mouse = Controller()
	time.sleep(3 + .0001 * random.randrange(1, 500))
	mouse.position = (786, 290)
	time.sleep(2 + .0001 * random.randrange(1, 500))
	mouse.click(Button.left, 1)

def coal():
	mouse = Controller()
	
	for i in range(100):
		for j in range(6):
			mine()
		dropLogs()

#cuts between two trees in var outside exchange. change whichTree to start at diff trees
def cutLogs():
	mouse = Controller()
	mouse.position = (818, 324)
	time.sleep(1 + .001 * random.randrange(1, 500))
	im = pyautogui.screenshot()
	if pyautogui.pixelMatchesColor(494, 80, (1, 213, 212), tolerance = 30):
		mouse.click(Button.left, 1)



def getMous():
	im = pyautogui.screenshot()
	print(im.getpixel((1133, 473)))


def main():
	logOut()
	# getMous()
	# getMous()
	# minecoal()
	# fastminecoal()
	# dropLogs()
	mineEss()
	print("hi")

main()


	

