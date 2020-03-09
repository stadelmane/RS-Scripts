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

	log = pyautogui.locateOnScreen('Screenshots/log.png' , confidence = .9)
	print(log)
	if log:
		realmouse.move_mouse_to(random.randrange(log[0] + 3, log[0] + log[2] - 3) , 
			random.randrange(log[1] + 3, log[1] + log[3] - 3))
		mouse.click(Button.left, 1)
		time.sleep(1 + .0001 * random.randrange(1, 500))

	log = pyautogui.locateOnScreen('Screenshots/logout.png' , confidence = .9)
	if log:
		realmouse.move_mouse_to(random.randrange(log[0] + 3, log[0] + log[2] - 3) , 
			random.randrange(log[1] + 3, log[1] + log[3] - 3))
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
	itterations = input("How many itterations: ")
	for i in range(itterations):
		if random.randrange(0, 100) == 68:
				skillcheck('minning')
		rock1 = pyautogui.locateOnScreen('Screenshots/rock1.png', confidence = .70)
		if rock1:
			realmouse.move_mouse_to(random.randrange(rock1[0] , rock1[0] + rock1[2]) , random.randrange(rock1[1] + 3 , rock1[1] + rock1[3]))
			mouse.click(Button.left, 1)
			while(rock1):
				rock1 = pyautogui.locateOnScreen('Screenshots/rock1.png', confidence = .70)

		rock2 = pyautogui.locateOnScreen('Screenshots/rock2.png', confidence = .70)
		if rock2:
			realmouse.move_mouse_to(random.randrange(rock2[0] , rock2[0] + rock2[2]) , random.randrange(rock2[1] + 3 , rock2[1] + rock2[3]))
			mouse.click(Button.left, 1)
			while(rock2):
				rock2 = pyautogui.locateOnScreen('Screenshots/rock1.png', confidence = .70)
		

		rock3 = pyautogui.locateOnScreen('Screenshots/rock3.png', confidence = .70)
		if rock3:
			realmouse.move_mouse_to(random.randrange(rock3[0] , rock3[0] + rock3[2]) , random.randrange(rock3[1] + 3 , rock3[1] + rock3[3]))
			mouse.click(Button.left, 1)
			while(rock3):
				rock3 = pyautogui.locateOnScreen('Screenshots/rock1.png', confidence = .70)
		

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

def skillcheck(skill):
	mouse = Controller()
	skillTab = pyautogui.locateOnScreen('Screenshots/skillTab.png', confidence = .70)
	if skillTab:
		realmouse.move_mouse_to( random.randrange(skillTab[0] + 2, skillTab[0] + skillTab[2] - 2) , random.randrange(skillTab[1] + 2 , skillTab[1] + skillTab[3] - 2) )
		mouse.click(Button.left, 1)
	
	skill = pyautogui.locateOnScreen('Screenshots/' + skill + '.png' , confidence = .50)
	if skill:
		realmouse.move_mouse_to( random.randrange(skill[0] + 2, skill[0] + skill[2] - 2) , random.randrange(skill[1] + 2 , skill[1] + skill[3] - 2) )
		time.sleep(3 + .0001 * random.randrange(1, 500))
	
	inv = pyautogui.locateOnScreen('Screenshots/inv.png', confidence = .70)
	if inv:
		realmouse.move_mouse_to( random.randrange(inv[0] + 2, inv[0] + inv[2] - 2) , random.randrange(inv[1] + 2 , inv[1] + inv[3] - 2) )
		mouse.click(Button.left, 1)	
	else:
		logout()

def test():
	inviron = pyautogui.locateOnScreen('Screenshots/inviron.png', confidence = .70)
	print(inviron)

def train():
	mouse = Controller()
	trout = pyautogui.locateOnScreen('Screenshots/trout.png', confidence = .70)
	while trout:
		
		health = pyautogui.locateOnScreen('Screenshots/heart.png', confidence = .90)
		if health:
			trout = pyautogui.locateOnScreen('Screenshots/trout.png', confidence = .70)
			if trout:
				realmouse.move_mouse_to( random.randrange(trout[0], trout[0] + trout[2]) , random.randrange(trout[1] + 2, trout[1] + trout[3] - 2))
				mouse.click(Button.left, 1)
				time.sleep(3 + .0001 * random.randrange(1, 500))


	


def cannonBall():
	mouse = Controller()
	ironnote = pyautogui.locateOnScreen('Screenshots/ironnote.png', confidence = .70)

	while(ironnote):
		furnace = None
		startcannonballs = None
		smeltingConfirmation = None
		cannonTeller = None
		yes = None

		furnace = pyautogui.locateOnScreen('Screenshots/furnace.png', confidence = .7)
		cannonTeller = pyautogui.locateOnScreen('Screenshots/cannonTeller.png', confidence = .70)
		smelting = pyautogui.locateOnScreen('Screenshots/smelting.png', confidence = .80)

		while (not furnace):
			print("here")
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
			if random.randrange(0, 1000) == 68:
				skillcheck('minning')

		while (not cannonTeller):
			cannonTeller = pyautogui.locateOnScreen('Screenshots/cannonTeller.png', confidence = .70)
		
		ironnote = pyautogui.locateOnScreen('Screenshots/ironnote.png', confidence = .70)
		if (ironnote):
			realmouse.move_mouse_to(random.randrange(ironnote[0] + 1, ironnote[0] + ironnote[2] - 1) , random.randrange(ironnote[1] + 1 , ironnote[1] + ironnote[3] - 1))
			mouse.click(Button.left, 1)

			realmouse.move_mouse_to(random.randrange(cannonTeller[0] + 15 , cannonTeller[0] + cannonTeller[2] - 5) , random.randrange(cannonTeller[1] + 5, cannonTeller[1] + cannonTeller[3] - 5))
			mouse.click(Button.left, 1)
		else:
			logOut()

		time.sleep(4)
		cannonTeller = pyautogui.locateOnScreen('Screenshots/cannonTeller.png', confidence = .70)
		yes = pyautogui.locateOnScreen('Screenshots/yes.png', confidence = .70)
		if (not yes and cannonTeller):
			realmouse.move_mouse_to(random.randrange(ironnote[0] + 1, ironnote[0] + ironnote[2] - 1) , random.randrange(ironnote[1] + 1 , ironnote[1] + ironnote[3] - 1))
			mouse.click(Button.left, 1)

			realmouse.move_mouse_to(random.randrange(cannonTeller[0] + 15 , cannonTeller[0] + cannonTeller[2] - 5) , random.randrange(cannonTeller[1] + 5, cannonTeller[1] + cannonTeller[3] - 5))
			mouse.click(Button.left, 1)
		while (not yes):
			yes = pyautogui.locateOnScreen('Screenshots/yes.png', confidence = .70)

		realmouse.move_mouse_to(random.randrange(yes[0] , yes[0] + yes[2]) , random.randrange(yes[1] + 3 , yes[1] + yes[3]))
		mouse.click(Button.left, 1)
		# time.sleep(1.5)
		# inviron = pyautogui.locateOnScreen('Screenshots/inviron.png', confidence = .70)
		# if (not inviron):
		# 	realmouse.move_mouse_to(random.randrange(yes[0] , yes[0] + yes[2]) , random.randrange(yes[1] + 3 , yes[1] + yes[3]))
		# 	mouse.click(Button.left, 1)
		# 	inviron = pyautogui.locateOnScreen('Screenshots/inviron.png', confidence = .70)
		# 	time.sleep(1.5)
		# if (not inviron):
		# 	logOut()

		



def main():

	# getMous()
	# getMous()
	minecoal()
	# fastminecoal()
	# dropLogs()
	# mineEss()
	# string()
	#test()
	# skillcheck('minning')
	# cannonBall()
	logOut()
	#train()

	# mineEss()

main()


	

