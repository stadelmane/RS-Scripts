from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
from Custom_Modules import realmouse
from threading import Thread

import webbrowser
import time
import random
import pyautogui

def logOut():
	mouse = MouseController()
	print("starting logout!")
	log = pyautogui.locateOnScreen('Screenshots/logout/log.png' , confidence = .9)
	print(log)
	if log:
		realmouse.move_mouse_to(random.randrange(log[0] + 3, log[0] + log[2] - 3) , 
			random.randrange(log[1] + 3, log[1] + log[3] - 3))
		mouse.click(Button.left, 1)
		time.sleep(1 + .0001 * random.randrange(1, 500))

	log = pyautogui.locateOnScreen('Screenshots/logout/logout.png' , confidence = .9)
	if log:
		realmouse.move_mouse_to(random.randrange(log[0] + 3, log[0] + log[2] - 3) , 
			random.randrange(log[1] + 3, log[1] + log[3] - 3))
		mouse.click(Button.left, 1)	

def missclickLeft(x , y):
	mouse = MouseController()
	print('fail left')
	pyautogui.moveTo(random.randrange((x - 25), (x - 10)) , random.randrange(y, y+8) , randTime())
	mouse.click(Button.left, 1)
	return

def missclickRight(x , y):
	mouse = MouseController()
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
	keyboard = KeyboardController()
	mouse = MouseController()
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
			if (random.choice(['click' , 'space' , 0 , 0])) == 'click':
				x3 , y3 = stringCord(Xthree , Ythree)
				realmouse.move_mouse_to(x3 , y3)
				mouse.click(Button.left, 1)
			if (random.choice(['click' , 'space' , 0 , 0])) == 'space':
				time.sleep(.1 * random.randrange(10, 21))
				keyboard.press(' ')
				keyboard.release(' ')
			else:
				time.sleep(.1 * random.randrange(10, 21))
				keyboard.press('1')
				keyboard.release('1')

def invFull(item, folder, quantity):
	invItem = list(pyautogui.locateAllOnScreen('Screenshots/' + folder + '/' + item + '.png', confidence = .70))
	if len(invItem) >= quantity:
		return True
	else:
		return False

def minecoal():
	failures = 0
	mouse = MouseController()
	rock1 = pyautogui.locateOnScreen('Screenshots/coalMining/rock1.png', confidence = .70)
	rock2 = pyautogui.locateOnScreen('Screenshots/coalMining/rock2.png', confidence = .70)
	rock3 = pyautogui.locateOnScreen('Screenshots/coalMining/rock3.png', confidence = .70)
	itterations = input("How many itterations: ")
	for i in range(int(itterations)):
		if random.randrange(0, 100) == 68:
				skillcheck('mining')

		failures = 0
		rock1 = pyautogui.locateOnScreen('Screenshots/coalMining/rock1.png', confidence = .95)
		if rock1:
			pos = clickPos(rock1 , 20 , 20)
			realmouse.move_mouse_to(pos[0], pos[1])
			mouse.click(Button.left, 1)

			while(rock1):
				# time.sleep(.25)
				rock1 = pyautogui.locateOnScreen('Screenshots/coalMining/rock1.png', grayscale = False, confidence = .95)
				failures +=1
				if failures > 10:
					rock1 = False
				print('here1')
		if invFull('ironoreInv' , 'coalMining' , 20):
			dropItem('ironoreInv' , 'coalMining')

		failures = 0
		rock2 = pyautogui.locateOnScreen('Screenshots/coalMining/rock2.png', confidence = .9)
		if rock2:
			pos = clickPos(rock2 , 20 , 20)
			realmouse.move_mouse_to(pos[0], pos[1])
			mouse.click(Button.left, 1)
			while(rock2):
				# time.sleep(.25)
				rock2 = pyautogui.locateOnScreen('Screenshots/coalMining/rock2.png', grayscale = False, confidence = .95)
				failures +=1
				if failures > 10:
					rock2 = False
				print('here2')

		failures = 0
		rock3 = pyautogui.locateOnScreen('Screenshots/coalMining/rock3.png', confidence = .85)
		if rock3:
			pos = clickPos(rock3 , 20 , 5)
			realmouse.move_mouse_to(pos[0], pos[1])
			mouse.click(Button.left, 1)
			while(rock3):
				# time.sleep(.25)
				rock3 = pyautogui.locateOnScreen('Screenshots/coalMining/rock3.png', grayscale = False, confidence = .95)
				failures +=1
				if failures > 10:
					rock3 = False
				print('here3')

def dropItem(item, folder):
	mouse = MouseController()
	inv = list(pyautogui.locateAllOnScreen('Screenshots/' + folder + '/' + item + '.png', confidence = .70))
	for obj in inv:
		pos = clickPos(obj, 3 , 3)
		realmouse.move_mouse_to(pos[0], pos[1])
		mouse.click(Button.left, 1)

def skillcheck(skill):
	mouse = MouseController()
	skillTab = pyautogui.locateOnScreen('Screenshots/skillcheck/skillTab.png', confidence = .70)
	if skillTab:
		realmouse.move_mouse_to( random.randrange(skillTab[0] + 2, skillTab[0] + skillTab[2] - 2) , random.randrange(skillTab[1] + 2 , skillTab[1] + skillTab[3] - 2) )
		mouse.click(Button.left, 1)
	
	skill = pyautogui.locateOnScreen('Screenshots/skillcheck/' + skill + '.png' , confidence = .50)
	if skill:
		realmouse.move_mouse_to( random.randrange(skill[0] + 2, skill[0] + skill[2] - 2) , random.randrange(skill[1] + 2 , skill[1] + skill[3] - 2) )
		time.sleep(3 + .0001 * random.randrange(1, 500))
	
	inv = pyautogui.locateOnScreen('Screenshots/skillcheck/inv.png', confidence = .70)
	if inv:
		realmouse.move_mouse_to( random.randrange(inv[0] + 2, inv[0] + inv[2] - 2) , random.randrange(inv[1] + 2 , inv[1] + inv[3] - 2) )
		mouse.click(Button.left, 1)	
	else:
		logout()

def train():
	mouse = MouseController()
	tuna = pyautogui.locateOnScreen('Screenshots/cooking/tunaInv.png', confidence = .70)
	while tuna:
		health = pyautogui.locateOnScreen('Screenshots/training/heart.png', confidence = .85)
		if health:
			tuna = pyautogui.locateOnScreen('Screenshots/cooking/tunaInv.png', confidence = .70)
			if tuna:
				pos = clickPos(tuna[0] , 5 , 5)
				realmouse.move_mouse_to(pos[0] , pos[1])
				mouse.click(Button.left, 1)
				time.sleep(2)

def cannonBall():
	keyboard = KeyboardController()
	mouse = MouseController()
	ironnote = pyautogui.locateOnScreen('Screenshots/cannonBalls/ironnote.png', confidence = .70)

	while(ironnote):
		furnace = None
		startcannonballs = None
		smeltingConfirmation = None
		cannonTeller = None
		yes = None

		furnace = pyautogui.locateOnScreen('Screenshots/cannonBalls/furnace.png', confidence = .7)
		cannonTeller = pyautogui.locateOnScreen('Screenshots/cannonBalls/cannonTeller.png', confidence = .70)
		smelting = pyautogui.locateOnScreen('Screenshots/cannonBalls/smelting.png', confidence = .80)

		while (not furnace):
			print("here")
			furnace = pyautogui.locateOnScreen('Screenshots/cannonBalls/furnace.png', confidence = .7)
		if furnace:
			print('furnace')
			realmouse.move_mouse_to( random.randrange(furnace[0] + 2, furnace[0] + furnace[2] - 2) , random.randrange(furnace[1] + 2 , furnace[1] + furnace[3] - 2) )
			mouse.click(Button.left, 1)

		# waiting for cannonballs
		startcannonballs = pyautogui.locateOnScreen('Screenshots/cannonBalls/startcannonballs.png', confidence = .90)
		while (not startcannonballs):
			print("Waiting for cannon balls")
			startcannonballs = pyautogui.locateOnScreen('Screenshots/cannonBalls/startcannonballs.png', confidence = .90)

		# clicking to start cannon balls
		print("starting cannon balls")
		if (random.choice(['click' , 'space' , 0 , 0])) == 'click':
			pos = clickPos(startcannonballs, 5 , 5)
			realmouse.move_mouse_to(pos[0] , pos[1])
			mouse.click(Button.left, 1)
		if (random.choice(['click' , 'space' , 0 , 0])) == 'space':
			time.sleep(.1 * random.randrange(10, 21))
			keyboard.press(' ')
			keyboard.release(' ')
		else:
			time.sleep(.1 * random.randrange(10, 21))
			keyboard.press('1')
			keyboard.release('1')

		time.sleep(10)
		smeltingConfirmation = pyautogui.locateOnScreen('Screenshots/cannonBalls/smelting.png', confidence = .50)
		print(smeltingConfirmation)
		while(smeltingConfirmation):
			print("still smelting")
			smeltingConfirmation = pyautogui.locateOnScreen('Screenshots/cannonBalls/smelting.png', confidence = .50)
			if random.randrange(0, 1000) == 68:
				skillcheck('smithing')

		while (not cannonTeller):
			cannonTeller = pyautogui.locateOnScreen('Screenshots/cannonBalls/cannonTeller.png', confidence = .70)
		
		ironnote = pyautogui.locateOnScreen('Screenshots/cannonBalls/ironnote.png', confidence = .70)
		if (ironnote):
			pos = clickPos(ironnote, 1 , 1)
			realmouse.move_mouse_to(pos[0] , pos[1])
			mouse.click(Button.left, 1)

			realmouse.move_mouse_to(random.randrange(cannonTeller[0] + 15 , cannonTeller[0] + cannonTeller[2] - 5) , random.randrange(cannonTeller[1] + 5, cannonTeller[1] + cannonTeller[3] - 5))
			mouse.click(Button.left, 1)
		else:
			logOut()

		time.sleep(4)
		cannonTeller = pyautogui.locateOnScreen('Screenshots/cannonBalls/cannonTeller.png', confidence = .70)
		yes = pyautogui.locateOnScreen('Screenshots/cannonBalls/yes.png', confidence = .70)
		if (not yes and cannonTeller):
			realmouse.move_mouse_to(random.randrange(ironnote[0] + 1, ironnote[0] + ironnote[2] - 1) , random.randrange(ironnote[1] + 1 , ironnote[1] + ironnote[3] - 1))
			mouse.click(Button.left, 1)

			realmouse.move_mouse_to(random.randrange(cannonTeller[0] + 15 , cannonTeller[0] + cannonTeller[2] - 5) , random.randrange(cannonTeller[1] + 5, cannonTeller[1] + cannonTeller[3] - 5))
			mouse.click(Button.left, 1)
		while (not yes):
			yes = pyautogui.locateOnScreen('Screenshots/cannonBalls/yes.png', confidence = .70)

		#select yes with banker
		time.sleep(.1 * random.randrange(10, 21))
		keyboard.press('1')
		keyboard.release('1')


def clickPos(item, errorX, errorY):
	return random.randrange(item[0] + errorX , item[0] + item[2] - errorX) , random.randrange(item[1] + errorY , item[1] + item[3] - errorY)


'''food parameter is the food that you would like to be cooked.
must be in Rogue's Den facing North with 50% zoom
switch to modern layout to fit bank into frame
'''
def cooking(food):
	keyboard = KeyboardController()
	mouse = MouseController()
	failures = 0

	quantity = pyautogui.locateOnScreen('Screenshots/bank/all.png', confidence = .80)
	pos = clickPos(quantity, 2 , 2)
	realmouse.move_mouse_to(pos[0] , pos[1])
	mouse.click(Button.left, 1)

	bankFish = pyautogui.locateOnScreen('Screenshots/cooking/' + food + 'Bank.png', confidence = .90)
	pos = clickPos(bankFish, 3 , 5)
	realmouse.move_mouse_to(pos[0] , pos[1])
	mouse.click(Button.left, 1)

	closeBank = pyautogui.locateOnScreen('Screenshots/cooking/closeBank.png', confidence = .80)
	pos = clickPos(closeBank, 3 , 5)
	realmouse.move_mouse_to(pos[0] , pos[1])
	mouse.click(Button.left, 1)

	fire = pyautogui.locateOnScreen('Screenshots/cooking/fire.png', confidence = .80)
	while not fire:
		fire = pyautogui.locateOnScreen('Screenshots/cooking/fire.png', confidence = .74)
		failures += 1
		if failures > 10:
			print("Couldn't find fire")

	itterations = input("Enter how many itterations: ")

	for i in range(int(itterations)):

		fishies = list(pyautogui.locateAllOnScreen('Screenshots/cooking/' + food + 'Inv.png', confidence = .90))
		if len(fishies) != 28:
			fishies = list(pyautogui.locateAllOnScreen('Screenshots/cooking/' + food + 'Inv.png', confidence = .90))
		fish = random.choice(fishies)
		pos = clickPos(fish , 4 , 5)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)
		
		pos = clickPos(fire, 5 , 5)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)

		failures = 1
		start = pyautogui.locateOnScreen('Screenshots/cooking/' + food + 'Start.png', confidence = .80)
		while not start:
			start = pyautogui.locateOnScreen('Screenshots/cooking/' + food + 'Start.png', confidence = .80)
			failures += 1
			if failures % 20 == 0:
				pos = clickPos(fish , 4 , 5)
				realmouse.move_mouse_to(pos[0] , pos[1])
				mouse.click(Button.left, 1)

				pos = clickPos(fire, 0 , 0)
				realmouse.move_mouse_to(pos[0] , pos[1])
				mouse.click(Button.left, 1)

		keyboard.press('1')
		keyboard.release('1')

		cooked = False
		lvlUp = pyautogui.locateOnScreen('Screenshots/lvlUp.png', confidence = .80)
		while not lvlUp and not cooked:
			time.sleep(1)
			lvlUp = pyautogui.locateOnScreen('Screenshots/lvlUp.png', confidence = .80)
			fishies = list(pyautogui.locateAllOnScreen('Screenshots/cooking/' + food + 'Inv.png', confidence = .90))
			if len(fishies) == 0:
				cooked = True
			if lvlUp:
				while lvlUp:
					pos = clickPos(lvlUp, 2 , 1)
					realmouse.move_mouse_to(pos[0] , pos[1])
					mouse.click(Button.left, 1)

					pos = clickPos(fire, 0 , 0)
					realmouse.move_mouse_to(pos[0] , pos[1])
					time.sleep(3)
					lvlUp = pyautogui.locateOnScreen('Screenshots/lvlUp.png', confidence = .80)
				lvlUp = True

		bank = pyautogui.locateOnScreen('Screenshots/cooking/bank.png', confidence = .80)
		while not bank:
			bank = pyautogui.locateOnScreen('Screenshots/cooking/bank.png', confidence = .77)
			print("cant find bank")
		pos = clickPos(bank, 5 , 5)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)

		emptyInv = pyautogui.locateOnScreen('Screenshots/cooking/emptyInv.png', confidence = .90)
		while not emptyInv:
			emptyInv = pyautogui.locateOnScreen('Screenshots/cooking/emptyInv.png', confidence = .90)
		pos = clickPos(emptyInv, 3 , 5)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)

		pos = clickPos(bankFish, 3 , 5)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)

		pos = clickPos(closeBank, 3 , 5)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)

		
def arrowshaft():
	keyboard = KeyboardController()
	mouse = MouseController()
	input('press enter on banker')
	Xone , Yone = int((mouse.position)[0]) , int((mouse.position)[1])
	
	iters = int(input("Please enter how many iterations: "))
	for i in range(iters):
		print(i)

		#click on knife
		knife = pyautogui.locateOnScreen('Screenshots/arrowshaft/knife.png', confidence = .80)
		pos = clickPos(knife, 3 , 5)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)

		#click on log
		logs = list(pyautogui.locateAllOnScreen('Screenshots/arrowshaft/logInv.png', confidence = .95))
		pos = clickPos(logs[random.randrange(0, len(logs)-1)] , 3 , 5)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)

		#select arrow shafts to create
		time.sleep(.1 * random.randrange(10, 21))
		keyboard.press('1')
		keyboard.release('1')

		while logs:
			logs = list(pyautogui.locateAllOnScreen('Screenshots/arrowshaft/logInv.png', confidence = .95))

		#click on noted logs
		notedLogs = pyautogui.locateOnScreen('Screenshots/arrowshaft/notedLogs.png', confidence = .80)
		pos = clickPos(notedLogs, 3 , 5)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)

		#click on banker
		x1 , y1 = stringCord(Xone , Yone)
		realmouse.move_mouse_to(x1 , y1)
		mouse.click(Button.left, 1)

		#select yes with banker
		time.sleep(.1 * random.randrange(10, 21))
		keyboard.press('1')
		keyboard.release('1')

def sandCrabs():
	keyboard = KeyboardController()
	mouse = MouseController()
	print("starting")
	for i in range(int(input('Please how many cycles: '))):

		step1 = pyautogui.locateOnScreen('Screenshots/sandCrabs/step1.png', confidence = .70)
		while not step1:
			step1 = pyautogui.locateOnScreen('Screenshots/sandCrabs/step1.png', confidence = .70)
		pos = clickPos(step1, 3 , 5)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)
		time.sleep(5)

		step2 = pyautogui.locateOnScreen('Screenshots/sandCrabs/step2.png', confidence = .70)
		while not step2:
			step2 = pyautogui.locateOnScreen('Screenshots/sandCrabs/step2.png', confidence = .70)
			print('step2')
		step2 = [step2[0] , step2[1] , int(step2[2] * .3) , step2[3]]
		pos = clickPos(step2, 0 , 8)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)
		time.sleep(7)

		farthestPoint = pyautogui.locateOnScreen('Screenshots/sandCrabs/farthestPoint.png', confidence = .70)
		while not farthestPoint:
			farthestPoint = pyautogui.locateOnScreen('Screenshots/sandCrabs/farthestPoint.png', confidence = .70)
			print('farthestPoint')
		pos = clickPos(farthestPoint, 10 , 10)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)
		time.sleep(5)

		#begin run back
		step3 = pyautogui.locateOnScreen('Screenshots/sandCrabs/step3.png', confidence = .7)
		stepThree = pyautogui.locateOnScreen('Screenshots/sandCrabs/stepThree.png', confidence = .7)
		while not step3 and not stepThree:
			print('step3')
			step3 = pyautogui.locateOnScreen('Screenshots/sandCrabs/step3.png', confidence = .7)
			stepThree = pyautogui.locateOnScreen('Screenshots/sandCrabs/stepThree.png', confidence = .7)
		if step3:
			pos = clickPos(step3, 10 , 10)
		else:
			pos = clickPos(stepThree, 10 , 10)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)
		time.sleep(4.5)

		step4 = pyautogui.locateOnScreen('Screenshots/sandCrabs/step4.png', confidence = .70)
		while not step4:
			step4 = pyautogui.locateOnScreen('Screenshots/sandCrabs/step4.png', confidence = .70)
			print('step4')
		pos = clickPos(step4, 10 , 10)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)
		time.sleep(4.5)

		step5 = pyautogui.locateOnScreen('Screenshots/sandCrabs/step5.png', confidence = .70)
		while not step5:
			step5 = pyautogui.locateOnScreen('Screenshots/sandCrabs/step5.png', confidence = .70)
		pos = clickPos(step5, 10 , 10)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)
		time.sleep(5)

		step6 = pyautogui.locateOnScreen('Screenshots/sandCrabs/step6.png', confidence = .70)
		while not step6:
			step6 = pyautogui.locateOnScreen('Screenshots/sandCrabs/step6.png', confidence = .70)
		pos = clickPos(step6, 10 , 10)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)
		time.sleep(5)

		destination = pyautogui.locateOnScreen('Screenshots/sandCrabs/destination.png', confidence = .70)
		while not destination:
			destination = pyautogui.locateOnScreen('Screenshots/sandCrabs/destination.png', confidence = .70)
		pos = clickPos(destination, 5 , 5)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)

		sleepTime = random.randrange(54, 61)
		for x in range(0, sleepTime):
			print(sleepTime - x)
			time.sleep(10)

def splash():
	mouse = MouseController()
	monk1 = pyautogui.locateOnScreen('Screenshots/splash/monk1.png', confidence = .70)
	monk2 = pyautogui.locateOnScreen('Screenshots/splash/monk2.png', confidence = .70)
	blankSpace = pyautogui.locateOnScreen('Screenshots/splash/blankSpace.png', confidence = .70)
	while True:
		monk1, monk2 = None, None
		monk1 = pyautogui.locateOnScreen('Screenshots/splash/monk1.png', confidence = .70)
		monk2 = pyautogui.locateOnScreen('Screenshots/splash/monk2.png', confidence = .70)
		if monk1:
			pos = clickPos(monk1, 5 , 8)
			realmouse.move_mouse_to(pos[0] , pos[1])
			mouse.click(Button.left, 1)
		if monk2:
			pos = clickPos(monk2, 5 , 10)
			realmouse.move_mouse_to(pos[0] , pos[1])
			mouse.click(Button.left, 1)
		time.sleep(1)
		pos = clickPos(blankSpace, 5 , 8)
		realmouse.move_mouse_to(pos[0] , pos[1])

		magicIcon = pyautogui.locateOnScreen('Screenshots/splash/magicIcon.png', confidence = .90)
		while magicIcon:
			time.sleep(1)
			if random.randrange(1, 140) == 68:
				skillcheck('magic')
			
			if random.randrange(1, 30) == 25:
				monk2 = pyautogui.locateOnScreen('Screenshots/splash/monk2.png', confidence = .70)
				if monk2:
					pos = clickPos(monk2, 5 , 10)
					realmouse.move_mouse_to(pos[0] , pos[1])
					mouse.click(Button.left, 1)
				pos = clickPos(blankSpace, 5 , 8)
				realmouse.move_mouse_to(pos[0] , pos[1])
			print("Casting")
			magicIcon = pyautogui.locateOnScreen('Screenshots/splash/magicIcon.png', confidence = .90)

def trainMagic():
	t = Thread(target=splash)
	t.daemon = True
	t.start()
	time.sleep(4500)


def hotWater():
	mouse = MouseController()

	input('press enter on banker')
	Xone , Yone = int((mouse.position)[0]) , int((mouse.position)[1])

	input('press enter when bank tab is opened')

	hot_water_bank = pyautogui.locateOnScreen('Screenshots/hotWater/hotWaterBank.png', confidence = .90)
	empty_cup_bank = pyautogui.locateOnScreen('Screenshots/hotWater/emptyCupBank.png', confidence = .90)
	close_bank = pyautogui.locateOnScreen('Screenshots/cooking/closeBank.png', confidence = .80)
	empty_inv = pyautogui.locateOnScreen('Screenshots/cooking/emptyInv.png', confidence = .95)

	while True:
		pos = clickPos(close_bank, 4 , 4)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)
		time.sleep(1)
		empty_cup_inv = list(pyautogui.locateAllOnScreen('Screenshots/hotWater/emptyCupInv.png', confidence = .90))
		hot_water_inv = list(pyautogui.locateAllOnScreen('Screenshots/hotWater/hotWaterInv.png', confidence = .90))
		for i in range(14):
			cup = random.choice(empty_cup_inv)
			water = random.choice(hot_water_inv)
			
			empty_cup_inv.remove(cup)
			hot_water_inv.remove(water)

			pos = clickPos(cup, 4 , 4)
			realmouse.move_mouse_to(pos[0] , pos[1])
			mouse.click(Button.left, 1)

			pos = clickPos(water, 4 , 4)
			realmouse.move_mouse_to(pos[0] , pos[1])
			mouse.click(Button.left, 1)
		#click on banker
		x1 , y1 = stringCord(Xone , Yone)
		realmouse.move_mouse_to(x1 , y1)
		mouse.click(Button.left, 1)
		time.sleep(2)

		#empty Inv 
		empty_inv = pyautogui.locateOnScreen('Screenshots/cooking/emptyInv.png', confidence = .95)
		pos = clickPos(empty_inv, 4 , 4)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)

		pos = clickPos(empty_cup_bank, 4 , 4)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)

		pos = clickPos(hot_water_bank, 4 , 4)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)


def ranarr():
	mouse = MouseController()

	input('press enter on banker')
	Xone , Yone = int((mouse.position)[0]) , int((mouse.position)[1])

	input('press enter when bank tab is opened')

	quantity = pyautogui.locateOnScreen('Screenshots/bank/all.png', confidence = .80)
	grimmy_ranarr_bank = pyautogui.locateOnScreen('Screenshots/herb/grimmyRanarrBank.png', confidence = .90)
	close_bank = pyautogui.locateOnScreen('Screenshots/cooking/closeBank.png', confidence = .80)
	empty_inv = pyautogui.locateOnScreen('Screenshots/cooking/emptyInv.png', confidence = .95)

	pos = clickPos(quantity, 2 , 2)
	realmouse.move_mouse_to(pos[0] , pos[1])
	mouse.click(Button.left, 1)
	notDone = True
	while notDone:
		pos = clickPos(grimmy_ranarr_bank, 4 , 4)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)

		pos = clickPos(close_bank, 4 , 4)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)
		time.sleep(1)
		grimmy_ranarr_inv = list(pyautogui.locateAllOnScreen('Screenshots/herb/grimmyRanarrInv.png', confidence = .97))
		if len(grimmy_ranarr_inv) < 28:
			notDone = False
		for i in range(len(grimmy_ranarr_inv)):
			pos = clickPos(grimmy_ranarr_inv[i], 4 , 4)
			realmouse.move_mouse_to(pos[0] , pos[1])
			mouse.click(Button.left, 1)

		#click on banker
		x1 , y1 = stringCord(Xone , Yone)
		realmouse.move_mouse_to(x1 , y1)
		mouse.click(Button.left, 1)
		time.sleep(2)

		#empty Inv 
		pos = clickPos(empty_inv, 4 , 4)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)

def potion():
	keyboard = KeyboardController()
	mouse = MouseController()

	input('press enter on banker')
	Xone , Yone = int((mouse.position)[0]) , int((mouse.position)[1])

	input('press enter when bank tab is opened')
	quantity = pyautogui.locateOnScreen('Screenshots/bank/x.png', confidence = .80)
	waterVialBank = pyautogui.locateOnScreen('Screenshots/herb/waterVialBank.png', confidence = .99)
	cleanRanarrBank = pyautogui.locateOnScreen('Screenshots/herb/cleanRanarr.png', confidence = .98)
	close_bank = pyautogui.locateOnScreen('Screenshots/cooking/closeBank.png', confidence = .80)
	empty_inv = pyautogui.locateOnScreen('Screenshots/cooking/emptyInv.png', confidence = .95)
	
	pos = clickPos(quantity, 2 , 2)
	realmouse.move_mouse_to(pos[0] , pos[1])
	mouse.click(Button.left, 1)

	while True:
		pos = clickPos(waterVialBank, 4 , 4)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)

		pos = clickPos(cleanRanarrBank, 4 , 4)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)

		pos = clickPos(close_bank, 4 , 4)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)
		time.sleep(.5)
		cleanRanarrInv = list(pyautogui.locateAllOnScreen('Screenshots/herb/cleanRanarrInv.png', confidence = .90))
		waterVialInv = list(pyautogui.locateAllOnScreen('Screenshots/herb/waterVialInv.png', confidence = .90))
			
		ranarr = random.choice(cleanRanarrInv)
		vial = random.choice(waterVialInv)
			

		pos = clickPos(ranarr, 4 , 4)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)

		pos = clickPos(vial, 4 , 4)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)

		if (random.choice(['click' , 'space' , 0 , 0])) == 'space':
			time.sleep(.1 * random.randrange(10, 21))
			keyboard.press(' ')
			keyboard.release(' ')
		else:
			time.sleep(.1 * random.randrange(10, 21))
			keyboard.press('1')
			keyboard.release('1')

		time.sleep(9)

		#click on banker
		x1 , y1 = stringCord(Xone , Yone)
		realmouse.move_mouse_to(x1 , y1)
		mouse.click(Button.left, 1)

		#empty Inv 
		pos = clickPos(empty_inv, 4 , 4)
		realmouse.move_mouse_to(pos[0] , pos[1])
		time.sleep(.5)
		mouse.click(Button.left, 1)



def ranarrPotion():
	mouse = MouseController()
	keyboard = KeyboardController()

	input('press enter on banker')
	Xone , Yone = int((mouse.position)[0]) , int((mouse.position)[1])

	input('press enter when bank tab is opened')

	quantity = pyautogui.locateOnScreen('Screenshots/bank/x.png', confidence = .80)
	grimmy_ranarr_bank = pyautogui.locateOnScreen('Screenshots/herb/grimmyRanarrBank.png', confidence = .90)
	waterVialBank = pyautogui.locateOnScreen('Screenshots/herb/waterVialBank.png', confidence = .99)
	close_bank = pyautogui.locateOnScreen('Screenshots/cooking/closeBank.png', confidence = .80)
	empty_inv = pyautogui.locateOnScreen('Screenshots/cooking/emptyInv.png', confidence = .95)

	pos = clickPos(quantity, 2 , 2)
	realmouse.move_mouse_to(pos[0] , pos[1])
	mouse.click(Button.left, 1)
	notDone = True
	while notDone:
		pos = clickPos(grimmy_ranarr_bank, 4 , 4)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)

		pos = clickPos(waterVialBank, 2 , 2)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)

		pos = clickPos(close_bank, 4 , 4)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)
		time.sleep(1)

		grimmy_ranarr_inv = list(pyautogui.locateAllOnScreen('Screenshots/herb/grimmyRanarrInv.png', confidence = .97))
		waterVialInv = list(pyautogui.locateAllOnScreen('Screenshots/herb/waterVialInv.png', confidence = .90))
			

		if len(grimmy_ranarr_inv) < 14:
			notDone = False
		for i in range(len(grimmy_ranarr_inv)):
			pos = clickPos(grimmy_ranarr_inv[i], 4 , 4)
			realmouse.move_mouse_to(pos[0] , pos[1])
			mouse.click(Button.left, 1)

		ranarr = random.choice(grimmy_ranarr_inv[0 : len(grimmy_ranarr_inv)-2])
		vial = random.choice(waterVialInv)
		pos = clickPos(ranarr, 4 , 4)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)

		pos = clickPos(vial, 4 , 4)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)
		
		if (random.choice(['click' , 'space' , 0 , 0])) == 'space':
			time.sleep(.1 * random.randrange(10, 21))
			keyboard.press(' ')
			keyboard.release(' ')
		else:
			time.sleep(.1 * random.randrange(10, 21))
			keyboard.press('1')
			keyboard.release('1')
		time.sleep(9)

		#click on banker
		x1 , y1 = stringCord(Xone , Yone)
		realmouse.move_mouse_to(x1 , y1)
		mouse.click(Button.left, 1)
		time.sleep(.75)

		#empty Inv 
		pos = clickPos(empty_inv, 4 , 4)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)

def test():
	mouse = MouseController()
	keyboard = KeyboardController()
	print("\a")

def fireMaking():
	mouse = MouseController()
	keyboard = KeyboardController()

	tele = pyautogui.locateOnScreen('Screenshots/tele/varrock.png', confidence = .80)
	tinderBox = pyautogui.locateOnScreen('Screenshots/fireMaking/tinderBox.png', confidence = .80)
	notedLogs = list(pyautogui.locateAllOnScreen('Screenshots/fireMaking/notedLogs.png', confidence = .90))

	
	while notedLogs:
		yes = None
		lit = None
		time.sleep(1)
		logs = list(pyautogui.locateAllOnScreen('Screenshots/fireMaking/logs.png', confidence = .80))
		print(len(logs))
		notedLogs = list(pyautogui.locateAllOnScreen('Screenshots/fireMaking/notedLogs.png', confidence = .90))
		pos = clickPos(tele, 4 , 4)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)
		toggle = pyautogui.locateOnScreen('Screenshots/fireMaking/toggleOn.png', confidence = .90)
		if toggle:
			pos = clickPos(toggle, 4 , 4)
			realmouse.move_mouse_to(pos[0] , pos[1])
			mouse.click(Button.left, 1)
		time.sleep(4)
		spot1 = pyautogui.locateOnScreen('Screenshots/fireMaking/spot1.png', confidence = .70)
		spot2 = pyautogui.locateOnScreen('Screenshots/fireMaking/spot2.png', confidence = .70)
		spot3 = pyautogui.locateOnScreen('Screenshots/fireMaking/spot3.png', confidence = .70)
		if spot1:
			pos = clickPos(spot1, 10 , 10)
			realmouse.move_mouse_to(pos[0] , pos[1])
			mouse.click(Button.left, 1)
		elif spot2:
			pos = clickPos(spot2, 10 , 10)
			realmouse.move_mouse_to(pos[0] , pos[1])
			mouse.click(Button.left, 1)
		elif spot3:
			pos = clickPos(spot3, 10 , 10)
			realmouse.move_mouse_to(pos[0] , pos[1])
			mouse.click(Button.left, 1)
		else:
			print("Couldn't find spot to begin")
			logOut()
		time.sleep(2)

		endScript = 0
		for i in range(len(logs)):
			lit = None
			log = random.choice(logs)
			logs.remove(log)
			pos = clickPos(tinderBox, 4 , 4)
			realmouse.move_mouse_to(pos[0] , pos[1])
			mouse.click(Button.left, 1)

			pos = clickPos(log, 4 , 4)
			realmouse.move_mouse_to(pos[0] , pos[1])
			mouse.click(Button.left, 1)
			print(lit)
			time.sleep(1.25)
			failures = 0
			logs2 = list(pyautogui.locateAllOnScreen('Screenshots/fireMaking/logs.png', confidence = .80))
			while len(logs) != len(logs2):
				failures += 1
				logs2 = list(pyautogui.locateAllOnScreen('Screenshots/fireMaking/logs.png', confidence = .80))
				pos = clickPos(tinderBox, 4 , 4)
				realmouse.move_mouse_to(pos[0] , pos[1])
				mouse.click(Button.left, 1)
				pos = clickPos(log, 4 , 4)
				realmouse.move_mouse_to(pos[0] , pos[1])
				mouse.click(Button.left, 1)
				time.sleep(1)
				if failures == 3:
					endScript += 1
					logs2 = list(pyautogui.locateAllOnScreen('Screenshots/fireMaking/logs.png', confidence = .80))
					logs = list(pyautogui.locateAllOnScreen('Screenshots/fireMaking/logs.png', confidence = .80))
				if endScript == 3:
					logOut()
					quit()



			# lit = pyautogui.locateOnScreen('Screenshots/fireMaking/lit.png', confidence = .85)
			# counter = 1
			# while not lit:
			# 	counter +=1
			# 	lit = pyautogui.locateOnScreen('Screenshots/fireMaking/lit.png', confidence = .90)
			# 	if counter % 50 == 0:
			# 		pos = clickPos(tinderBox, 4 , 4)
			# 		realmouse.move_mouse_to(pos[0] , pos[1])
			# 		mouse.click(Button.left, 1)
			# 		pos = clickPos(log, 4 , 4)
			# 		realmouse.move_mouse_to(pos[0] , pos[1])
			# 		mouse.click(Button.left, 1)

		notedLogs = pyautogui.locateOnScreen('Screenshots/fireMaking/notedLogs.png', confidence = .80)
		pos = clickPos(notedLogs, 4 , 4)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)
		toggle = pyautogui.locateOnScreen('Screenshots/fireMaking/toggleOff.png', confidence = .90)
		pos = clickPos(toggle, 4 , 4)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)

		bank = pyautogui.locateOnScreen('Screenshots/fireMaking/bank.png', confidence = .65)
		bank2 = pyautogui.locateOnScreen('Screenshots/fireMaking/bank2.png', confidence = .70)
		if bank:
			pos = clickPos(bank, 3 , 3)
			realmouse.move_mouse_to(pos[0] , pos[1])
			mouse.click(Button.left, 1)
		elif bank2:
			pos = clickPos(bank2, 5 , 5)
			realmouse.move_mouse_to(pos[0] , pos[1])
			mouse.click(Button.left, 1)
		else:
			print("Couldn't find bank")
			logOut()

		counter=1
		while (not yes):
			counter+= 1
			yes = pyautogui.locateOnScreen('Screenshots/cannonBalls/yes.png', confidence = .70)
			if counter % 20 == 0:
				notedLogs = pyautogui.locateOnScreen('Screenshots/fireMaking/notedLogs.png', confidence = .80)
				pos = clickPos(notedLogs, 4 , 4)
				realmouse.move_mouse_to(pos[0] , pos[1])
				mouse.click(Button.left, 1)
				if bank:
					pos = clickPos(bank, 3 , 3)
					realmouse.move_mouse_to(pos[0] , pos[1])
					mouse.click(Button.left, 1)
				elif bank2:
					pos = clickPos(bank2, 5 , 5)
					realmouse.move_mouse_to(pos[0] , pos[1])
					mouse.click(Button.left, 1)

		keyboard.press('1')
		keyboard.release('1')

def pizza():
	keyboard = KeyboardController()
	mouse = MouseController()

	input('press enter on banker')
	Xone , Yone = int((mouse.position)[0]) , int((mouse.position)[1])

	input('press enter when bank tab is opened')
	quantity = pyautogui.locateOnScreen('Screenshots/bank/x.png', confidence = .80)
	pizzaBank = pyautogui.locateOnScreen('Screenshots/pizza/pizzaBank.png', confidence = .85)
	pineappleBank = pyautogui.locateOnScreen('Screenshots/pizza/pineappleBank.png', confidence = .85)
	close_bank = pyautogui.locateOnScreen('Screenshots/cooking/closeBank.png', confidence = .80)
	empty_inv = pyautogui.locateOnScreen('Screenshots/cooking/emptyInv.png', confidence = .85)
	
	pos = clickPos(quantity, 2 , 2)
	realmouse.move_mouse_to(pos[0] , pos[1])
	mouse.click(Button.left, 1)

	while True:
		pos = clickPos(pizzaBank, 4 , 4)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)

		pos = clickPos(pineappleBank, 4 , 4)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)

		pos = clickPos(close_bank, 4 , 4)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)
		time.sleep(.5)
		pizzaInv = list(pyautogui.locateAllOnScreen('Screenshots/pizza/pizzaInv.png', confidence = .85))
		pineappleInv = list(pyautogui.locateAllOnScreen('Screenshots/pizza/pineappleInv.png', confidence = .85))
			
		pizza = random.choice(pizzaInv)
		pineapple = random.choice(pineappleInv)
			
		with keyboard.pressed(Key.shift):
			pos = clickPos(pizza, 4 , 4)
			realmouse.move_mouse_to(pos[0] , pos[1])
			mouse.click(Button.left, 1)

			pos = clickPos(pineapple, 4 , 4)
			realmouse.move_mouse_to(pos[0] , pos[1])
			mouse.click(Button.left, 1)

		if (random.choice(['click' , 'space' , 0 , 0])) == 'space':
			time.sleep(.1 * random.randrange(10, 21))
			keyboard.press(' ')
			keyboard.release(' ')
		else:
			time.sleep(.1 * random.randrange(10, 21))
			keyboard.press('1')
			keyboard.release('1')

		time.sleep(17)

		#click on banker
		x1 , y1 = stringCord(Xone , Yone)
		realmouse.move_mouse_to(x1 , y1)
		mouse.click(Button.left, 1)

		#empty Inv 
		pos = clickPos(empty_inv, 4 , 4)
		realmouse.move_mouse_to(pos[0] , pos[1])
		time.sleep(.5)
		mouse.click(Button.left, 1)


def varrockAgility():
	keyboard = KeyboardController()
	mouse = MouseController()
	for i in range(int(input('Please how many cycles: '))):

		roof1 = pyautogui.locateOnScreen('Screenshots/varrockAgility/roof1.png', confidence = .70)
		roof1R = pyautogui.locateOnScreen('Screenshots/varrockAgility/roof1R.png', confidence = .70)
		while not roof1 and not roof1R:
			roof1 = pyautogui.locateOnScreen('Screenshots/varrockAgility/roof1.png', confidence = .70)
			roof1R = pyautogui.locateOnScreen('Screenshots/varrockAgility/roof1R.png', confidence = .70)
			print("roof1")
		if roof1R:
			print("\a")
			pos = clickPos(roof1R, 10 , 7)
		else:
			pos = clickPos(roof1, 10 , 7)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)
		time.sleep(8)

		roof2 = pyautogui.locateOnScreen('Screenshots/varrockAgility/roof2.png', confidence = .70)
		roof2R = pyautogui.locateOnScreen('Screenshots/varrockAgility/roof2R.png', confidence = .70)
		while not roof2 and not roof2R:
			roof2 = pyautogui.locateOnScreen('Screenshots/varrockAgility/roof2.png', confidence = .70)
			roof2R = pyautogui.locateOnScreen('Screenshots/varrockAgility/roof2R.png', confidence = .70)
			print("roof2")
		if roof2R:
			print("\a")
			pos = clickPos(roof2R, 10 , 7)
		else:
			pos = clickPos(roof2, 10 , 7)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)
		time.sleep(8)


		roof3 = pyautogui.locateOnScreen('Screenshots/varrockAgility/roof3.png', confidence = .70)
		roof3R = pyautogui.locateOnScreen('Screenshots/varrockAgility/roof3R.png', confidence = .70)
		while not roof3 and not roof3R:
			roof3 = pyautogui.locateOnScreen('Screenshots/varrockAgility/roof3.png', confidence = .70)
			roof3R = pyautogui.locateOnScreen('Screenshots/varrockAgility/roof3R.png', confidence = .70)
			print("roof3")
		if roof3R:
			print("\a")
			pos = clickPos(roof3R, 10 , 7)
		else:
			pos = clickPos(roof3, 7 , 7)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)
		time.sleep(12)

		roof4 = pyautogui.locateOnScreen('Screenshots/varrockAgility/roof4.png', confidence = .70)
		roof4R = pyautogui.locateOnScreen('Screenshots/varrockAgility/roof4R.png', confidence = .70)
		while not roof4 and not roof4R:
			roof4 = pyautogui.locateOnScreen('Screenshots/varrockAgility/roof4.png', confidence = .70)
			roof4R = pyautogui.locateOnScreen('Screenshots/varrockAgility/roof4R.png', confidence = .70)
			print("roof4")
		if roof4R:
			print("\a")
			pos = clickPos(roof4R, 10 , 7)
		else:
			pos = clickPos(roof4, 10 , 10)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)
		time.sleep(5)

		roof5 = pyautogui.locateOnScreen('Screenshots/varrockAgility/roof5.png', confidence = .70)
		roof5R = pyautogui.locateOnScreen('Screenshots/varrockAgility/roof5R.png', confidence = .70)
		while not roof5 and not roof5R:
			roof5 = pyautogui.locateOnScreen('Screenshots/varrockAgility/roof5.png', confidence = .70)
			roof5R = pyautogui.locateOnScreen('Screenshots/varrockAgility/roof5R.png', confidence = .70)
			print("roof5")
		if roof5R:
			print("\a")
			pos = clickPos(roof5R, 10 , 7)
		else:
			pos = clickPos(roof5, 7 , 7)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)
		time.sleep(8)


		roof6 = pyautogui.locateOnScreen('Screenshots/varrockAgility/roof6.png', confidence = .70)
		roof6R = pyautogui.locateOnScreen('Screenshots/varrockAgility/roof6R.png', confidence = .70)
		while not roof6 and not roof6R:
			roof6 = pyautogui.locateOnScreen('Screenshots/varrockAgility/roof6.png', confidence = .70)
			roof6R = pyautogui.locateOnScreen('Screenshots/varrockAgility/roof6R.png', confidence = .70)
			print("roof6")
		if roof6R:
			print("\a")
			pos = clickPos(roof6R, 10 , 7)
		else:
			pos = clickPos(roof6, 12 , 10)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)
		time.sleep(6.5)

		roof7 = pyautogui.locateOnScreen('Screenshots/varrockAgility/roof7.png', confidence = .70)
		roof7R = pyautogui.locateOnScreen('Screenshots/varrockAgility/roof7R.png', confidence = .70)
		while not roof7 and not roof7R:
			roof7 = pyautogui.locateOnScreen('Screenshots/varrockAgility/roof7.png', confidence = .70)
			roof7R = pyautogui.locateOnScreen('Screenshots/varrockAgility/roof7R.png', confidence = .70)
			print("roof7")
		if roof7R:
			print("\a")
			pos = clickPos(roof7R, 10 , 7)
		else:
			pos = clickPos(roof7, 7 , 7)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)
		time.sleep(6)

		roof8 = pyautogui.locateOnScreen('Screenshots/varrockAgility/roof8.png', confidence = .70)
		roof8R = pyautogui.locateOnScreen('Screenshots/varrockAgility/roof8R.png', confidence = .70)
		while not roof8 and not roof8R:
			roof8 = pyautogui.locateOnScreen('Screenshots/varrockAgility/roof8.png', confidence = .70)
			roof8R = pyautogui.locateOnScreen('Screenshots/varrockAgility/roof8R.png', confidence = .70)
			print("roof8")
		if roof8R:
			print("\a")
			pos = clickPos(roof8R, 10 , 7)
		else:
			pos = clickPos(roof8, 7 , 7)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)
		time.sleep(5)

		restart = pyautogui.locateOnScreen('Screenshots/varrockAgility/restart.png', confidence = .70)
		restartR = pyautogui.locateOnScreen('Screenshots/varrockAgility/restartR.png', confidence = .70)
		while not restart and not restartR:
			restart = pyautogui.locateOnScreen('Screenshots/varrockAgility/restart.png', confidence = .70)
			restartR = pyautogui.locateOnScreen('Screenshots/varrockAgility/restartR.png', confidence = .70)
		if restartR:
			print("\a")
			pos = clickPos(restartR, 10 , 7)
		else:
			pos = clickPos(restart, 7 , 5)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)
		time.sleep(10)

def nmz():
	keyboard = KeyboardController()
	mouse = MouseController()
	overload = list(pyautogui.locateAllOnScreen('Screenshots/nmz/overload.png', confidence = .96))
	absorptions = list(pyautogui.locateAllOnScreen('Screenshots/nmz/absorption.png', confidence = .96))
	print(len(absorptions))


	with keyboard.pressed(Key.shift):
		time.sleep(6)
		mouse.click(Button.left, 1)



def main():
	script = input("Please Enter which script you would like to run: ")
	if script == 'sandCrabs':
		sandCrabs()
	if script == 'minecoal':
		minecoal()
	if script == 'trainMagic':
		trainMagic()
	if script == 'hotWater':
		hotWater()
	if script == 'string':
		string()
	if script == 'cooking':
		cooking('lobster')
	if script == 'mining':
		skillcheck('mining')
	if script == 'cannonBall':
		cannonBall()
	if script == 'arrowshaft':
		arrowshaft()
	if script == 'pizza':
		pizza()
	if script == 'ranarrPotion':
		ranarrPotion()
	if script == 'fire':
		fireMaking()
	if script == 'agile':
		varrockAgility()
	if script == 'nmz':
		nmz()
	else:
		test()
	# logOut()	

main()
	

