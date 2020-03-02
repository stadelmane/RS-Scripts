from pynput.mouse import Button, Controller
from Custom_Modules import realmouse
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

	log = pyautogui.locateOnScreen('Screenshots/log.png' , confidence = .8)
	print(log)
	if log:
		pyautogui.moveTo(log[1], log[2], duration = (.2 + .01 * random.randrange(1, 5)))
		mouse.click(Button.left, 1)

	log = pyautogui.locateOnScreen('Screenshots/logout.png' , confidence = .8)
	print(log)
	if log:
		pyautogui.moveTo(log[1], log[2], duration = (.2 + .01 * random.randrange(1, 5)))
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
	for i in range(5):
		print("itteration: " , i)
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


def missclickLeft(x , y):
	mouse = Controller()
	print('fail left')
	pyautogui.moveTo(random.randrange((x - 25), (x - 10)) , random.randrange(y, y+8) , randTime())
	mouse.click(Button.left, 1)
	return

def missclickRight(x , y):
	mouse = Controller()
	print('fail right')
	pyautogui.moveTo(random.randrange(x + 30, x+ 50) , random.randrange(y, y+9) , randTime())
	mouse.click(Button.left, 1)
	return

def randTime():
	num = random.randrange(1, 1000)
	if num <= 900:
		return .275 + .001 * random.randrange(1, 100)
	if num <= 950:
		return .4 + .001 * random.randrange(1, 100)
	else:
		return random.randrange(5 , 7) * .01 + .001 * random.randrange(1, 100)

def stringCord(x , y):
	return random.randrange(x, x+10) , random.randrange(y, y+15)


def string():
	mouse = Controller()
	input('press enter on item 1!')
	Xone , Yone = int((mouse.position)[0]) , int((mouse.position)[1])

	input('press enter on item 2!')
	Xtwo , Ytwo = int((mouse.position)[0]) , int((mouse.position)[1])

	input('press enter on item 3!')
	Xthree , Ythree = int((mouse.position)[0]) , int((mouse.position)[1])
	
	iters = int(input("Please enter how many iterations: "))
	for i in range(iters):
		print(i)

		if random.randrange(1, 31) == 30:
			if random.randrange(1, 3) == 1:
				missclickLeft(Xtwo , Ytwo)
				pass
			else:
				x1 , y1 = stringCord(Xone , Yone)
				pyautogui.moveTo(x1 , y1 , randTime())
				mouse.click(Button.left, 1)
				missclickRight(Xone , Yone)
				pass
		else:
			x1 , y1 = stringCord(Xone , Yone)
			realmouse.move_mouse_to(x1 , y1)
			mouse.click(Button.left, 1)

			x2 , y2 = stringCord(Xtwo , Ytwo)
			realmouse.move_mouse_to(x2 , y2)
			time.sleep(random.randrange(11, 15) + .001 * random.randrange(1, 50))
			mouse.click(Button.left, 1)

			x3 , y3 = stringCord(Xthree , Ythree)
			realmouse.move_mouse_to(x3 , y3)
			mouse.click(Button.left, 1)






def minecoal():
	failures = 0
	mouse = Controller()
	im = pyautogui.screenshot()

	time.sleep(4 + .0001 * random.randrange(1, 500))


	input('press enter on rock 1!')
	rock1_x , rock1_y = int((mouse.position)[0]) , int((mouse.position)[1])

	input('press enter on rock 2!')
	rock2_x , rock2_y = int((mouse.position)[0]) , int((mouse.position)[1])

	input('press enter on rock 3!')
	rock3_x , rock3_y = int((mouse.position)[0]) , int((mouse.position)[1])
	rock1 = (im.getpixel((rock1_y, rock1_x)))
	rock2 = (im.getpixel((rock2_y, rock2_x)))
	rock3 = (im.getpixel((rock3_y, rock3_x)))

	print("error checking here!")



	for itterations in range(5000):
		failures = 0
		print("failing")
		print(pyautogui.pixelMatchesColor(rock1_x, rock1_y, (rock1[0], rock1[1], rock1[2]), tolerance =10))
		print(im.getpixel((rock1_y, rock1_x)))
		print(rock1[0], rock1[1], rock1[2])
		# im = pyautogui.screenshot()
		if pyautogui.pixelMatchesColor(rock1_x, rock1_y, (rock1[0], rock1[1], rock1[2]), tolerance =10):
			print("here1")
			x , y = coalpos(rock1_x , rock1_y)
			mouse.position = (x, y)
			time.sleep(.1 + .0001 * random.randrange(1, 500))
			mouse.click(Button.left, 2)
			while(pyautogui.pixelMatchesColor(rock1_x, rock1_y, (rock1[0], rock1[1], rock1[2]), tolerance =10)):
				failures += 1
				# im = pyautogui.screenshot()
				if failures % 6 == 0:
					mouse.click(Button.left, 1)

		failures = 0

		if pyautogui.pixelMatchesColor(rock2_x, rock2_y, (rock2[0], rock2[1], rock2[2]), tolerance =10):
			x , y = coalpos(rock2_x , rock2_y)
			mouse.position = (x, y)
			time.sleep(.1 + .0001 * random.randrange(1, 500))
			mouse.click(Button.left, 2)
			while(pyautogui.pixelMatchesColor(rock2_x, rock2_y, (rock2[0], rock2[1], rock2[2]), tolerance =10)):
				failures += 1
				# im = pyautogui.screenshot()
				if failures % 6 == 0:
					mouse.click(Button.left, 1)

		failures = 0

		if pyautogui.pixelMatchesColor(rock3_x, rock3_y, (rock3[0], rock3[1], rock3[2]), tolerance =10):
			x , y = coalpos(rock3_x , rock3_y)
			mouse.position = (x, y)
			time.sleep(.1 + .0001 * random.randrange(1, 500))
			mouse.click(Button.left, 2)
			while(pyautogui.pixelMatchesColor(rock3_x, rock3_y, (rock3[0], rock3[1], rock3[2]), tolerance =20)):
				failures += 1
				# im = pyautogui.screenshot()
				if failures % 6 == 0:
					mouse.click(Button.left, 1)

		failures = 0

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

def cannonBall():
	mouse = Controller()

	ironnote = pyautogui.locateOnScreen('Screenshots/ironnote.png', confidence = .70)

	while(True):
		furnace = None
		startcannonballs = None
		smeltingConfirmation = None
		cannonTeller = None
		yes = None

		furnace = pyautogui.locateOnScreen('Screenshots/furnace.png', confidence = .7)
		cannonTeller = pyautogui.locateOnScreen('Screenshots/cannonTeller.png', confidence = .70)
		smelting = pyautogui.locateOnScreen('Screenshots/smelting.png', confidence = .80)
		



		while (not furnace):
			furnace = pyautogui.locateOnScreen('Screenshots/furnace.png', confidence = .7)
		if furnace:
			print('furnace')
			realmouse.move_mouse_to( random.randrange(furnace[0] + 2, furnace[0] + furnace[2] - 2) , random.randrange(furnace[1] + 2 , furnace[1] + furnace[3] - 2) )
			mouse.click(Button.left, 1)

		# waiting for cannonballs
		startcannonballs = pyautogui.locateOnScreen('Screenshots/startcannonballs.png', confidence = .90)
		while (not startcannonballs):
			print("Waiting for cannon balls")
			startcannonballs = pyautogui.locateOnScreen('Screenshots/startcannonballs.png', confidence = .90)

		# clicking to start cannon balls
		print("starting cannon balls")
		realmouse.move_mouse_to( random.randrange(startcannonballs[0] + 5, startcannonballs[0] + startcannonballs[2] - 5) , 
			random.randrange(startcannonballs[1] + 5 , startcannonballs[1] + startcannonballs[3] - 5))
		mouse.click(Button.left, 1)

		time.sleep(10)
		smeltingConfirmation = pyautogui.locateOnScreen('Screenshots/smelting.png', confidence = .50)
		print(smeltingConfirmation)
		while(smeltingConfirmation):
			print("still smelting")
			smeltingConfirmation = pyautogui.locateOnScreen('Screenshots/smelting.png', confidence = .50)

		cannonTeller = pyautogui.locateOnScreen('Screenshots/cannonTeller.png', confidence = .70)
		if (cannonTeller):
			realmouse.move_mouse_to(random.randrange(ironnote[0] + 1, ironnote[0] + ironnote[2] - 1) , random.randrange(ironnote[1] + 1 , ironnote[1] + ironnote[3] - 1))
			mouse.click(Button.left, 1)

			realmouse.move_mouse_to(random.randrange(cannonTeller[0] + 15 , cannonTeller[0] + cannonTeller[2] - 5) , random.randrange(cannonTeller[1] + 5, cannonTeller[1] + cannonTeller[3] - 5))
			mouse.click(Button.left, 1)

		time.sleep(5)
		while (not yes):
			yes = pyautogui.locateOnScreen('Screenshots/yes.png', confidence = .70)
		if (yes):
			realmouse.move_mouse_to(random.randrange(yes[0] , yes[0] + yes[2]) , random.randrange(yes[1] + 3 , yes[1] + yes[3]))
			mouse.click(Button.left, 1)
		else:
			print("hi")



def main():
	# getMous()
	# getMous()
	# minecoal()
	# fastminecoal()
	# dropLogs()
	# mineEss()
	# string()
	cannonBall()

	# logOut()

	# mineEss()

main()


	

