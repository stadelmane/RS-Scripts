from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
from Custom_Modules import realmouse
from threading import Thread

import webbrowser
import time
import random
import pyautogui


keyboard = KeyboardController()
mouse = MouseController()
alchThread = True

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
	print("done with logout")

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
	sleep_time = 1.3
	inv_count = 0
	maxTime = False
	mouse = MouseController()
	rock1 = pyautogui.locateOnScreen('Screenshots/coalMining/rock1.png', confidence = .70)
	rock2 = pyautogui.locateOnScreen('Screenshots/coalMining/rock2.png', confidence = .70)
	rock3 = pyautogui.locateOnScreen('Screenshots/coalMining/rock3.png', confidence = .70)
	itterations = input("How many itterations: ")

	for i in range(int(itterations)):
		curr_count = list(pyautogui.locateAllOnScreen('Screenshots/coalMining/ironoreInv.png', confidence = .90))
		print(len(curr_count), inv_count)
		if inv_count + 3 == len(curr_count):
			sleep_time += -.005
			print(sleep_time)
		else:
			sleep_time += .005
			print("in else statement")
		if invFull('ironoreInv' , 'coalMining' , 20):
			dropItem('ironoreInv' , 'coalMining')

		inv_count = len(curr_count)



		if random.randrange(0, 100) == 68:
				skillcheck('mining')

		rock1 = pyautogui.locateOnScreen('Screenshots/coalMining/rock1.png', confidence = .90)
		while not rock1:
			pass
		pos = clickPos(rock1 , 20 , 20)
		realmouse.move_mouse_to(pos[0], pos[1])
		mouse.click(Button.left, 1)
		time.sleep(sleep_time)
			
		pos = clickPos(rock2 , 20 , 20)
		realmouse.move_mouse_to(pos[0], pos[1])
		mouse.click(Button.left, 1)
		time.sleep(sleep_time)
			

		pos = clickPos(rock3 , 20 , 5)
		realmouse.move_mouse_to(pos[0], pos[1])
		mouse.click(Button.left, 1)
		time.sleep(sleep_time)
			
	logOut()

def minecoalwa():
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
				time.sleep(.15)
				rock1 = pyautogui.locateOnScreen('Screenshots/coalMining/rock1.png', grayscale = False, confidence = .95)
				failures +=1
				if failures > 10:
					rock1 = False
		if invFull('ironoreInv' , 'coalMining' , 16):
			dropItem('ironoreInv' , 'coalMining')

		failures = 0
		rock2 = pyautogui.locateOnScreen('Screenshots/coalMining/rock2.png', confidence = .90)
		if rock2:
			pos = clickPos(rock2 , 20 , 20)
			realmouse.move_mouse_to(pos[0], pos[1])
			mouse.click(Button.left, 1)
			while(rock2):
				time.sleep(.15)
				rock2 = pyautogui.locateOnScreen('Screenshots/coalMining/rock2.png', grayscale = False, confidence = .90)
				failures +=1
				if failures > 10:
					rock2 = False

		failures = 0
		rock3 = pyautogui.locateOnScreen('Screenshots/coalMining/rock3.png', confidence = .90)
		if rock3:
			pos = clickPos(rock3 , 20 , 5)
			realmouse.move_mouse_to(pos[0], pos[1])
			mouse.click(Button.left, 1)
			while(rock3):
				time.sleep(.15)
				rock3 = pyautogui.locateOnScreen('Screenshots/coalMining/rock3.png', grayscale = False, confidence = .90)
				failures +=1
				if failures > 10:
					rock3 = False
	logOut()

def dropItem(item, folder):
	keyboard = KeyboardController()
	mouse = MouseController()
	inv = list(pyautogui.locateAllOnScreen('Screenshots/' + folder + '/' + item + '.png', confidence = .90))
	with keyboard.pressed(Key.shift):
		for obj in inv:
			pos = clickPos(obj, 3 , 3)
			realmouse.move_mouse_to(pos[0], pos[1])
			mouse.click(Button.left, 1)
		time.sleep(.2)


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
	itterations = input("Enter how many itterations: ")

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

	for i in range(int(itterations)):
		print("round: " , i)

		fishies = list(pyautogui.locateAllOnScreen('Screenshots/cooking/' + food + 'Inv.png', confidence = .90))
		while not fishies:
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
			fishies = list(pyautogui.locateAllOnScreen('Screenshots/cooking/' + food + 'Inv.png', confidence = .98))
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
	herb = input('1 for ranarr 2 for snapdragon: ')
	if herb == '1':
		herb = 'Ranarr'
	else:
		herb = 'Snapdragon'

	input('press enter on banker')
	Xone , Yone = int((mouse.position)[0]) , int((mouse.position)[1])

	input('press enter when bank tab is opened')

	quantity = pyautogui.locateOnScreen('Screenshots/bank/x.png', confidence = .80)
	# grimmy_ranarr_bank = pyautogui.locateOnScreen('Screenshots/herb/grimmy' + herb + 'Bank.png')
	waterVialBank = pyautogui.locateOnScreen('Screenshots/herb/waterVialBank.png', confidence = .99)
	close_bank = pyautogui.locateOnScreen('Screenshots/cooking/closeBank.png', confidence = .80)
	empty_inv = pyautogui.locateOnScreen('Screenshots/cooking/emptyInv.png', confidence = .95)
	grimmy_ranarr_inv = None
	waterVialInv = None


	pos = clickPos(quantity, 2 , 2)
	realmouse.move_mouse_to(pos[0] , pos[1])
	mouse.click(Button.left, 1)
	notDone = True
	while notDone:
		try:
			grimmy_ranarr_bank = pyautogui.locateOnScreen('Screenshots/herb/grimmy' + herb + 'Bank.png')

			if not grimmy_ranarr_bank:
				notDone = False
				pass

			pos = clickPos(grimmy_ranarr_bank, 4 , 4)
			realmouse.move_mouse_to(pos[0] , pos[1])
			mouse.click(Button.left, 1)

			pos = clickPos(waterVialBank, 2 , 2)
			realmouse.move_mouse_to(pos[0] , pos[1])
			mouse.click(Button.left, 1)

			pos = clickPos(close_bank, 4 , 4)
			realmouse.move_mouse_to(pos[0] , pos[1])
			mouse.click(Button.left, 1)
			# time.sleep(1)

			if not grimmy_ranarr_inv and not waterVialInv:
				grimmy_ranarr_inv = list(pyautogui.locateAllOnScreen('Screenshots/herb/grimmy' +  herb + 'Inv.png', confidence = .90))
				waterVialInv = list(pyautogui.locateAllOnScreen('Screenshots/herb/waterVialInv.png', confidence = .90))
				
			for i in range(len(grimmy_ranarr_inv)):
				pos = clickPos(grimmy_ranarr_inv[i], 4 , 4)
				realmouse.move_mouse_to(pos[0] , pos[1])
				mouse.click(Button.left, 1)

			# ranarr = random.choice(grimmy_ranarr_inv[0 : len(grimmy_ranarr_inv)-2])
			ranarr = grimmy_ranarr_inv[-1]
			vial = waterVialInv[0]
			# vial = random.choice(waterVialInv)

			pos = clickPos(vial, 4 , 4)
			realmouse.move_mouse_to(pos[0] , pos[1])
			mouse.click(Button.left, 1)
			
			pos = clickPos(ranarr, 4 , 4)
			realmouse.move_mouse_to(pos[0] , pos[1])
			mouse.click(Button.left, 1)
			
			if (random.choice(['click' , 'space' , 0 , 0])) == 'space':
				time.sleep(.075 * random.randrange(10, 21))
				keyboard.press(' ')
				keyboard.release(' ')
			else:
				time.sleep(.075 * random.randrange(10, 21))
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
		except:
			logOut()

def test():
	mouse = MouseController()
	keyboard = KeyboardController()

	Xone , Yone = int((mouse.position)[0]) , int((mouse.position)[1])
	while True:
		x1 , y1 = stringCord(Xone , Yone)
		realmouse.move_mouse_to(x1 , y1)
		mouse.click(Button.left, 1)

		time.sleep(random.randrange(20, 35))
	



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

		roof1 = pyautogui.locateOnScreen('Screenshots/agility/varrock/roof1.png', confidence = .85)
		roof1R = pyautogui.locateOnScreen('Screenshots/agility/varrock/roof1R.png', confidence = .85)
		while not roof1 and not roof1R:
			roof1 = pyautogui.locateOnScreen('Screenshots/agility/varrock/roof1.png', confidence = .80)
			roof1R = pyautogui.locateOnScreen('Screenshots/agility/varrock/roof1R.png', confidence = .80)
			print("roof1")
		if roof1R:
			print("\a")
			pos = clickPos(roof1R, 10 , 7)
		else:
			pos = clickPos(roof1, 10 , 7)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)
		time.sleep(8.5)

		roof2 = pyautogui.locateOnScreen('Screenshots/agility/varrock/roof2.png', confidence = .80)
		roof2R = pyautogui.locateOnScreen('Screenshots/agility/varrock/roof2R.png', confidence = .80)
		while not roof2 and not roof2R:
			roof2 = pyautogui.locateOnScreen('Screenshots/agility/varrock/roof2.png', confidence = .70)
			roof2R = pyautogui.locateOnScreen('Screenshots/agility/varrock/roof2R.png', confidence = .70)
			print("roof2")
		if roof2R:
			print("\a")
			pos = clickPos(roof2R, 7 , 3)
		else:
			pos = clickPos(roof2, 7 , 3)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)
		time.sleep(8)


		roof3 = pyautogui.locateOnScreen('Screenshots/agility/varrock/roof3.png', confidence = .70)
		roof3R = pyautogui.locateOnScreen('Screenshots/agility/varrock/roof3R.png', confidence = .70)
		while not roof3 and not roof3R:
			roof3 = pyautogui.locateOnScreen('Screenshots/agility/varrock/roof3.png', confidence = .70)
			roof3R = pyautogui.locateOnScreen('Screenshots/agility/varrock/roof3R.png', confidence = .70)
			print("roof3")
		if roof3R:
			print("\a")
			pos = clickPos(roof3R, 10 , 7)
		else:
			pos = clickPos(roof3, 7 , 7)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)
		time.sleep(12)

		roof4 = pyautogui.locateOnScreen('Screenshots/agility/varrock/roof4.png', confidence = .70)
		roof4R = pyautogui.locateOnScreen('Screenshots/agility/varrock/roof4R.png', confidence = .70)
		while not roof4 and not roof4R:
			roof4 = pyautogui.locateOnScreen('Screenshots/agility/varrock/roof4.png', confidence = .70)
			roof4R = pyautogui.locateOnScreen('Screenshots/agility/varrock/roof4R.png', confidence = .70)
			print("roof4")
		if roof4R:
			print("\a")
			pos = clickPos(roof4R, 25 , 7)
		else:
			pos = clickPos(roof4, 10 , 10)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)
		time.sleep(5)

		roof5 = pyautogui.locateOnScreen('Screenshots/agility/varrock/roof5.png', confidence = .70)
		roof5R = pyautogui.locateOnScreen('Screenshots/agility/varrock/roof5R.png', confidence = .70)
		while not roof5 and not roof5R:
			roof5 = pyautogui.locateOnScreen('Screenshots/agility/varrock/roof5.png', confidence = .70)
			roof5R = pyautogui.locateOnScreen('Screenshots/agility/varrock/roof5R.png', confidence = .70)
			print("roof5")
		if roof5R:
			print("\a")
			pos = clickPos(roof5R, 10 , 7)
		else:
			pos = clickPos(roof5, 7 , 7)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)
		time.sleep(8)


		roof6 = pyautogui.locateOnScreen('Screenshots/agility/varrock/roof6.png', confidence = .70)
		roof6R = pyautogui.locateOnScreen('Screenshots/agility/varrock/roof6R.png', confidence = .70)
		while not roof6 and not roof6R:
			roof6 = pyautogui.locateOnScreen('Screenshots/agility/varrock/roof6.png', confidence = .70)
			roof6R = pyautogui.locateOnScreen('Screenshots/agility/varrock/roof6R.png', confidence = .70)
			print("roof6")
		if roof6R:
			print("\a")
			pos = clickPos(roof6R, 10 , 7)
		else:
			pos = clickPos(roof6, 12 , 10)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)
		time.sleep(6.5)

		roof7 = pyautogui.locateOnScreen('Screenshots/agility/varrock/roof7.png', confidence = .70)
		roof7R = pyautogui.locateOnScreen('Screenshots/agility/varrock/roof7R.png', confidence = .70)
		while not roof7 and not roof7R:
			roof7 = pyautogui.locateOnScreen('Screenshots/agility/varrock/roof7.png', confidence = .70)
			roof7R = pyautogui.locateOnScreen('Screenshots/agility/varrock/roof7R.png', confidence = .70)
			print("roof7")
		if roof7R:
			print("\a")
			pos = clickPos(roof7R, 10 , 7)
		else:
			pos = clickPos(roof7, 7 , 7)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)
		time.sleep(6)

		roof8 = pyautogui.locateOnScreen('Screenshots/agility/varrock/roof8.png', confidence = .70)
		roof8R = pyautogui.locateOnScreen('Screenshots/agility/varrock/roof8R.png', confidence = .70)
		while not roof8 and not roof8R:
			roof8 = pyautogui.locateOnScreen('Screenshots/agility/varrock/roof8.png', confidence = .70)
			roof8R = pyautogui.locateOnScreen('Screenshots/agility/varrock/roof8R.png', confidence = .70)
			print("roof8")
		if roof8R:
			print("\a")
			pos = clickPos(roof8R, 10 , 7)
		else:
			pos = clickPos(roof8, 7 , 7)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)
		time.sleep(5)

		restart = pyautogui.locateOnScreen('Screenshots/agility/varrock/restart.png', confidence = .70)
		restartR = pyautogui.locateOnScreen('Screenshots/agility/varrock/restartR.png', confidence = .70)
		while not restart and not restartR:
			restart = pyautogui.locateOnScreen('Screenshots/agility/varrock/restart.png', confidence = .70)
			restartR = pyautogui.locateOnScreen('Screenshots/agility/varrock/restartR.png', confidence = .70)
		if restartR:
			print("\a")
			pos = clickPos(restartR, 10 , 7)
		else:
			pos = clickPos(restart, 7 , 5)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)
		time.sleep(11)

def canifisAgility():
	keyboard = KeyboardController()
	mouse = MouseController()
	while True:
		failures=0
		roof1 = pyautogui.locateOnScreen('Screenshots/agility/canifis/roof1.png', confidence = .80)
		roof1R = pyautogui.locateOnScreen('Screenshots/agility/canifis/roof1R.png', confidence = .85)
		while not roof1 and not roof1R:
			roof1 = pyautogui.locateOnScreen('Screenshots/agility/canifis/roof1.png', confidence = .70)
			roof1R = pyautogui.locateOnScreen('Screenshots/agility/canifis/roof1R.png', confidence = .70)
			print("roof1")
			failures+=1	
			if failures % 11 == 0:
				if reset():
					pass
		if roof1R:
			print("\a")
			pos = clickPos(roof1R, 5 , 5)
		else:
			pos = clickPos(roof1, 5 , 5)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)
		time.sleep(4)

		failures=0
		roof2 = pyautogui.locateOnScreen('Screenshots/agility/canifis/roof2.png', confidence = .80)
		roof2R = pyautogui.locateOnScreen('Screenshots/agility/canifis/roof2R.png', confidence = .80)
		while not roof2 and not roof2R:
			roof2 = pyautogui.locateOnScreen('Screenshots/agility/canifis/roof2.png', confidence = .70)
			roof2R = pyautogui.locateOnScreen('Screenshots/agility/canifis/roof2R.png', confidence = .70)
			print("roof2")
			failures+=1	
			if failures % 11 == 0:
				if reset():
					pass
		if roof2R:
			pos = clickPos(roof2R, 5 , 3)
		else:
			pos = clickPos(roof2, 5 , 3)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)
		time.sleep(5)

		failures=0
		roof3 = pyautogui.locateOnScreen('Screenshots/agility/canifis/roof3.png', confidence = .80)
		roof3R = pyautogui.locateOnScreen('Screenshots/agility/canifis/roof3R.png', confidence = .80)
		while not roof3 and not roof3R:
			roof3 = pyautogui.locateOnScreen('Screenshots/agility/canifis/roof3.png', confidence = .80)
			roof3R = pyautogui.locateOnScreen('Screenshots/agility/canifis/roof3R.png', confidence = .80)
			print("roof3")
			failures+=1	
			if failures % 11 == 0:
				if reset():
					pass
		if roof3R:
			x , y = pyautogui.locateCenterOnScreen('Screenshots/agility/canifis/roof3R.png', confidence = .75)
			realmouse.move_mouse_to(x , y)
			# pos = clickPos(roof3R, 5 , 5)
		else:
			x , y = pyautogui.locateCenterOnScreen('Screenshots/agility/canifis/roof3.png', confidence = .75)
			realmouse.move_mouse_to(x , y)
			# pos = clickPos(roof3, 5 , 5)
		# realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)
		time.sleep(4.25)

		failures=0
		roof4 = pyautogui.locateOnScreen('Screenshots/agility/canifis/roof4.png', confidence = .80)
		roof4R = pyautogui.locateOnScreen('Screenshots/agility/canifis/roof4R.png', confidence = .80)
		while not roof4 and not roof4R:
			roof4 = pyautogui.locateOnScreen('Screenshots/agility/canifis/roof4.png', confidence = .80)
			roof4R = pyautogui.locateOnScreen('Screenshots/agility/canifis/roof4R.png', confidence = .80)
			print("roof4")
			failures+=1	
			if failures % 11 == 0:
				if reset():
					pass
		if roof4R:
			x , y = pyautogui.locateCenterOnScreen('Screenshots/agility/canifis/roof4R.png', confidence = .75)
			realmouse.move_mouse_to(x , y)
			# pos = clickPos(roof4R, 5 , 5)
		else:
			x , y = pyautogui.locateCenterOnScreen('Screenshots/agility/canifis/roof4.png', confidence = .75)
			realmouse.move_mouse_to(x ,y)
			# pos = clickPos(roof4, 5 , 5)
		# realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)
		time.sleep(5)

		failures=0
		roof5 = pyautogui.locateOnScreen('Screenshots/agility/canifis/roof5.png', confidence = .80)
		roof5R = pyautogui.locateOnScreen('Screenshots/agility/canifis/roof5R.png', confidence = .70)
		while not roof5 and not roof5R:
			roof5 = pyautogui.locateOnScreen('Screenshots/agility/canifis/roof5.png', confidence = .70)
			roof5R = pyautogui.locateOnScreen('Screenshots/agility/canifis/roof5R.png', confidence = .70)
			print("roof5")
			failures+=1	
			if failures % 11 == 0:
				if reset():
					pass
		if roof5R:
			pos = clickPos(roof5R, 5 , 5)
		else:
			pos = clickPos(roof5, 5 , 5)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)
		time.sleep(6)


		failures=0
		roof6 = pyautogui.locateOnScreen('Screenshots/agility/canifis/roof6.png', confidence = .80)
		roof6R = pyautogui.locateOnScreen('Screenshots/agility/canifis/roof6R.png', confidence = .75)
		roof6Glitch = pyautogui.locateOnScreen('Screenshots/agility/canifis/roofGlitch.png', confidence = .80)
		roof6RGlitch = pyautogui.locateOnScreen('Screenshots/agility/canifis/roofGlitchR.png', confidence = .80)
		while not roof6 and not roof6R and not roof6Glitch and not roof6RGlitch:
			roof6 = pyautogui.locateOnScreen('Screenshots/agility/canifis/roof6.png', confidence = .75)
			roof6R = pyautogui.locateOnScreen('Screenshots/agility/canifis/roof6R.png', confidence = .75)
			roof6Glitch = pyautogui.locateOnScreen('Screenshots/agility/canifis/roofGlitch.png', confidence = .75)
			roof6RGlitch = pyautogui.locateOnScreen('Screenshots/agility/canifis/roofGlitchR.png', confidence = .75)
			print("roof6")
			failures+=1	
			if failures % 11 == 0:
				if reset():
					pass
		if roof6R:
			x , y = pyautogui.locateCenterOnScreen('Screenshots/agility/canifis/roof6R.png', confidence = .75)
			realmouse.move_mouse_to(x , y)
			# realmouse.move_mouse_to(roof6R[0] , roof6R[1])
			# pos = clickPos(roof6R, 5 , 5)
		elif roof6RGlitch:
			pos = clickPos(roof6RGlitch, 5 , 5)
			realmouse.move_mouse_to(pos[0] , pos[1])
		elif roof6Glitch:
			pos = clickPos(roof6Glitch, 5 , 5)
			realmouse.move_mouse_to(pos[0] , pos[1])
		else:
			x , y = pyautogui.locateCenterOnScreen('Screenshots/agility/canifis/roof6.png', confidence = .75)
			realmouse.move_mouse_to(x , y)
			# pos = clickPos(roof6, 5 , 5)
		
		mouse.click(Button.left, 1)
		time.sleep(5.75)

		failures=0
		roof7 = pyautogui.locateOnScreen('Screenshots/agility/canifis/roof7.png', confidence = .80)
		roof7R = pyautogui.locateOnScreen('Screenshots/agility/canifis/roof7R.png', confidence = .70)
		while not roof7 and not roof7R:
			roof7 = pyautogui.locateOnScreen('Screenshots/agility/canifis/roof7.png', confidence = .70)
			roof7R = pyautogui.locateOnScreen('Screenshots/agility/canifis/roof7R.png', confidence = .70)
			print("roof7")
			failures+=1	
			if failures % 11 == 0:
				if reset():
					pass
		if roof7R:
			pos = clickPos(roof7R, 5 , 5)
		else:
			pos = clickPos(roof7, 5 , 5)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)
		time.sleep(5)

		failures=0
		restart = pyautogui.locateOnScreen('Screenshots/agility/canifis/restart.png', confidence = .80)
		restartR = pyautogui.locateOnScreen('Screenshots/agility/canifis/restartR.png', confidence = .70)
		while not restart and not restartR:
			restart = pyautogui.locateOnScreen('Screenshots/agility/canifis/restart.png', confidence = .70)
			restartR = pyautogui.locateOnScreen('Screenshots/agility/canifis/restartR.png', confidence = .70)
			failures+=1	
			if failures % 11 == 0:
				if reset():
					pass
		if restartR:
			pos = clickPos(restartR, 5 , 5)
		else:
			pos = clickPos(restart, 5 , 5)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)
		time.sleep(5)

def reset():
	print("\a")
	print("\a")
	print("\a")
	response = input("Would you like to reset the script? y or n")
	if response == 'y':
		return True
	else:
		return False

def nmz():
	keyboard = KeyboardController()
	mouse = MouseController()
	overload = list(pyautogui.locateAllOnScreen('Screenshots/nmz/overload.png', confidence = .96))
	absorptions = list(pyautogui.locateAllOnScreen('Screenshots/nmz/absorption.png', confidence = .96))
	prayer = pyautogui.locateOnScreen('Screenshots/nmz/prayer.png', confidence = .70)
	outside = pyautogui.locateOnScreen('Screenshots/nmz/outside.png', confidence = .70)
	print(len(absorptions))
	total_time = 300
	counter = 0
	while not outside:
		outside = pyautogui.locateOnScreen('Screenshots/nmz/outside.png', confidence = .70)

		time_to_sleep = random.randrange(15, 40)
		print(total_time + time_to_sleep)
		if outside:
			pass
		if total_time + time_to_sleep > 300:
			
			time.sleep(301 - total_time)
			pos = clickPos(prayer, 3 , 3)
			realmouse.move_mouse_to(pos[0] , pos[1])
			mouse.click(Button.left, 1)
			time.sleep(.5)
			mouse.click(Button.left, 1)


			overloadPot = overload[counter // 4]
			counter += 1
			pos = clickPos(overloadPot, 3 , 3)
			realmouse.move_mouse_to(pos[0] , pos[1])
			mouse.click(Button.left, 1)

			

			total_time = 0

		else:
			total_time += time_to_sleep + .5
			time.sleep(time_to_sleep)
			pos = clickPos(prayer, 3 , 3)
			realmouse.move_mouse_to(pos[0] , pos[1])
			mouse.click(Button.left, 1)
			time.sleep(random.randrange(2 , 4) * .1)
			mouse.click(Button.left, 1)
	logOut()

def cannon():
	mouse = MouseController()
	keyboard = KeyboardController()
	input("click hereto begin")
	Xone , Yone = int((mouse.position)[0]) , int((mouse.position)[1])
	while True:
		x1 , y1 = stringCord(Xone , Yone)
		realmouse.move_mouse_to(x1 , y1)
		mouse.click(Button.left, 1)

		time.sleep(random.randrange(20, 35))

def treecutting():
	mouse = MouseController()
	tree = pyautogui.locateOnScreen('Screenshots/treecutting/tree.png', confidence = .75)
	while True:
		pos = clickPos(tree, 3 , 3)
		realmouse.move_mouse_to(pos[0] , pos[1])
		# mouse.click(Button.left, 1)
		# time.sleep(1)
		chopTree = pyautogui.locateOnScreen('Screenshots/treecutting/chopTree.png', confidence = .75)
		while not chopTree:
			chopTree = pyautogui.locateOnScreen('Screenshots/treecutting/chopTree.png', confidence = .75)

		# if chopTree:
		mouse.click(Button.left, 1)
		while chopTree:
			chopTree = pyautogui.locateOnScreen('Screenshots/treecutting/chopTree.png', confidence = .75)
			logs = list(pyautogui.locateAllOnScreen('Screenshots/treecutting/logsInv.png', confidence = .90))
			lvlUp = pyautogui.locateOnScreen('Screenshots/lvlUp.png', confidence = .80)
			if lvlUp:
				chopTree = None
			if len(logs) >= 27:
				dropItem('logsInv' , 'treecutting')
				chopTree = None
				logs = []
		if len(logs) > 8:
			print()
			dropItem('logsInv' , 'treecutting')

def gem():
	keyboard = KeyboardController()
	mouse = MouseController()

	rock = input("Please enter the correct stone: \n 1: Opal \n 2: Sapphire \n 3: Emerald")
	if rock == "1":
		rock = "opal"
		print("Screenshots not taken yet")
	if rock == "2":
		rock = 'sapphire'
		print("getting here!")
	if rock == "3":
		rock = "emerald"

	input('press enter on banker')
	Xone , Yone = int((mouse.position)[0]) , int((mouse.position)[1])

	input('press enter when bank tab is opened')
	quantity = pyautogui.locateOnScreen('Screenshots/bank/all.png', confidence = .80)
	
	chisel_bank = pyautogui.locateOnScreen('Screenshots/gem/chiselBank.png', confidence = .85)
	gem_bank = pyautogui.locateOnScreen('Screenshots/gem/' + rock + 'Bank.png', confidence = .85)
	close_bank = pyautogui.locateOnScreen('Screenshots/cooking/closeBank.png', confidence = .80)
	empty_inv = pyautogui.locateOnScreen('Screenshots/cooking/emptyInv.png', confidence = .85)
	
	pos = clickPos(quantity, 2 , 2)
	realmouse.move_mouse_to(pos[0] , pos[1])
	mouse.click(Button.left, 1)

	while True:
		pos = clickPos(chisel_bank, 4 , 4)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)

		pos = clickPos(gem_bank, 4 , 4)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)

		pos = clickPos(close_bank, 4 , 4)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)
		time.sleep(1)
		chisel = list(pyautogui.locateOnScreen('Screenshots/gem/chiselInv.png', confidence = .85))
		gem = list(pyautogui.locateAllOnScreen('Screenshots/gem/' + rock + 'Inv.png', confidence = .85))
			

		gem = random.choice(gem)
			
		pos = clickPos(chisel, 4 , 4)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)

		pos = clickPos(gem, 4 , 4)
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

		time.sleep(33)

		#click on banker
		x1 , y1 = stringCord(Xone , Yone)
		realmouse.move_mouse_to(x1 , y1)
		mouse.click(Button.left, 1)

		#empty Inv 
		pos = clickPos(empty_inv, 4 , 4)
		realmouse.move_mouse_to(pos[0] , pos[1])
		time.sleep(.5)
		mouse.click(Button.left, 1)

def flyFish():
	while True:
		spot = pyautogui.locateOnScreen('Screenshots/fishing/salmon.png', confidence = .9)
		pos = clickPos(spot, 4 , 4)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)
		time.sleep(3)
		not_fishing = pyautogui.locateOnScreen('Screenshots/fishing/notFishing.png', confidence = .70)
		while not not_fishing:
			not_fishing = pyautogui.locateOnScreen('Screenshots/fishing/notFishing.png', confidence = .70)




def spinFlax():
	mouse = MouseController()
	keyboard = KeyboardController()

	input('press enter on banker')
	Xone , Yone = int((mouse.position)[0]) , int((mouse.position)[1])

	input('press enter when bank tab is opened')

	quantity = pyautogui.locateOnScreen('Screenshots/bank/all.png', confidence = .80)

	flax = pyautogui.locateOnScreen('Screenshots/spinFlax/flax.png', confidence = .90)
	close_bank = pyautogui.locateOnScreen('Screenshots/cooking/closeBank.png', confidence = .80)

	pos = clickPos(quantity, 2 , 2)
	realmouse.move_mouse_to(pos[0] , pos[1])
	mouse.click(Button.left, 1)
	notDone = True

	pos = clickPos(flax, 4 , 4)
	realmouse.move_mouse_to(pos[0] , pos[1])
	mouse.click(Button.left, 1)

	pos = clickPos(close_bank, 4 , 4)
	realmouse.move_mouse_to(pos[0] , pos[1])
	mouse.click(Button.left, 1)
	time.sleep(1)

	mage = pyautogui.locateOnScreen('Screenshots/spinFlax/magicBook.png', confidence = .90)
	pos = clickPos(mage, 4 , 4)
	realmouse.move_mouse_to(pos[0] , pos[1])
	mouse.click(Button.left, 1)
	time.sleep(1)

	#first pass
	spell = pyautogui.locateOnScreen('Screenshots/spinFlax/spell.png', confidence = .80)
	pos = clickPos(spell, 4 , 4)
	realmouse.move_mouse_to(pos[0] , pos[1])

	for i in range(5):
		mouse.click(Button.left, 1)
		time.sleep(3)

	#click on banker
	x1 , y1 = stringCord(Xone , Yone)
	realmouse.move_mouse_to(x1 , y1)
	mouse.click(Button.left, 1)
	time.sleep(1.5)

	strings = list(pyautogui.locateAllOnScreen('Screenshots/spinFlax/string.png', confidence = .85))
	string = random.choice(strings)
		
	#empty Inv 
	pos = clickPos(string, 4 , 4)
	realmouse.move_mouse_to(pos[0] , pos[1])
	mouse.click(Button.left, 1) 

	#more flax
	pos = clickPos(flax, 4 , 4)
	realmouse.move_mouse_to(pos[0] , pos[1])
	mouse.click(Button.left, 1)

	#close bank
	pos = clickPos(close_bank, 4 , 4)
	realmouse.move_mouse_to(pos[0] , pos[1])
	mouse.click(Button.left, 1)
	time.sleep(1)

	for i in range(1500):
		try:
			pos = clickPos(spell, 4 , 4)
			realmouse.move_mouse_to(pos[0] , pos[1])

			for i in range(5):
				mouse.click(Button.left, 1)
				time.sleep(3)

			#click on banker
			x1 , y1 = stringCord(Xone , Yone)
			realmouse.move_mouse_to(x1 , y1)
			mouse.click(Button.left, 1)
			time.sleep(.5)

			string = random.choice(strings)
				
			#empty Inv 
			pos = clickPos(string, 4 , 4)
			realmouse.move_mouse_to(pos[0] , pos[1])
			mouse.click(Button.left, 1) 
			flax = pyautogui.locateOnScreen('Screenshots/spinFlax/flax.png', confidence = .90)

			#more flax
			pos = clickPos(flax, 4 , 4)
			realmouse.move_mouse_to(pos[0] , pos[1])
			mouse.click(Button.left, 1)

			#close bank
			pos = clickPos(close_bank, 4 , 4)
			realmouse.move_mouse_to(pos[0] , pos[1])
			mouse.click(Button.left, 1)
			time.sleep(1)
		except:
			notDone = False
			close_bank = pyautogui.locateOnScreen('Screenshots/cooking/closeBank.png', confidence = .80)
			if close_bank:
				pos = clickPos(close_bank, 4 , 4)
				realmouse.move_mouse_to(pos[0] , pos[1])
				mouse.click(Button.left, 1)
				time.sleep(1)
			logOut()


def acceptSupplies(trade_request = None):
	#hit trade button
	if trade_request == None:
		trade_request = pyautogui.locateOnScreen('Screenshots/trade/initiateTrade.png', confidence = .90)
		while not trade_request:
			trade_request = pyautogui.locateOnScreen('Screenshots/trade/initiateTrade.png', confidence = .90)
			print("waiting for trade request to be sent")
	
	pos = clickPos(trade_request, 4 , 2)
	realmouse.move_mouse_to(pos[0] , pos[1])
	mouse.click(Button.left, 1)

	waitingForPlayer = pyautogui.locateOnScreen('Screenshots/trade/waitingForPlayer.png', confidence = .90)
	while not waitingForPlayer:
		waitingForPlayer = pyautogui.locateOnScreen('Screenshots/trade/waitingForPlayer.png', confidence = .90)
		print("waiting for other player to accept")

	
	accept = pyautogui.locateOnScreen('Screenshots/trade/accept.png', confidence = .90)
	pos = clickPos(accept, 4 , 4)
	realmouse.move_mouse_to(pos[0] , pos[1])
	mouse.click(Button.left, 1)
	

	secondMenu = pyautogui.locateOnScreen('Screenshots/trade/secondMenu.png', confidence = .90)
	while not secondMenu:
		secondMenu = pyautogui.locateOnScreen('Screenshots/trade/secondMenu.png', confidence = .90)
		print("waiting for other player to accept")

	accept = pyautogui.locateOnScreen('Screenshots/trade/accept.png', confidence = .90)
	pos = clickPos(accept, 4 , 4)
	realmouse.move_mouse_to(pos[0] , pos[1])
	mouse.click(Button.left, 1)
	time.sleep(1 + .0001 * random.randrange(1, 500))

	while accept:
		accept = pyautogui.locateOnScreen('Screenshots/trade/accept.png', confidence = .90)		

def faceNorth():
	compass = pyautogui.locateOnScreen('Screenshots/misc/compass.png', confidence = .70)
	pos = clickPos(compass, 4 , 4)
	realmouse.move_mouse_to(pos[0] , pos[1])
	mouse.click(Button.left, 1)

def lookStraight():
	try:
		keyboard.press(Key.down)
		time.sleep(1.5)
		keyboard.release(Key.down)
	except AttributeError:
		print("Error in looking straight call")




def AIOHerbs(type):
	if type == "consumer":
		acceptSupplies()
	else:
		#ensure entity hider is on
		pass

	time.sleep(1 + .0001 * random.randrange(1, 500))

	#set up screen
	faceNorth()
	lookStraight()
	print("done setting up screen")

	time.sleep(.5)
	bankTeller = pyautogui.locateOnScreen('Screenshots/herb/bankTeller.png', confidence = .80)
	Xone , Yone = int(bankTeller[0]) , int(bankTeller[1] + bankTeller[3] * .5)

	#click on banker
	x1 , y1 = stringCord(Xone , Yone)
	realmouse.move_mouse_to(x1 , y1)
	mouse.click(Button.left, 1)
	time.sleep(5)

	quantity = pyautogui.locateOnScreen('Screenshots/bank/x.png', confidence = .80)
	waterVialBank = pyautogui.locateOnScreen('Screenshots/herb/waterVialBank.png', confidence = .99)
	close_bank = pyautogui.locateOnScreen('Screenshots/cooking/closeBank.png', confidence = .80)
	empty_inv = pyautogui.locateOnScreen('Screenshots/cooking/emptyInv.png', confidence = .95)
	grimmy_ranarr_inv = None
	waterVialInv = None

	#empty Inv 
	pos = clickPos(empty_inv, 4 , 4)
	realmouse.move_mouse_to(pos[0] , pos[1])
	mouse.click(Button.left, 1)

	time.sleep(2)

	pos = clickPos(quantity, 2 , 2)
	realmouse.move_mouse_to(pos[0] , pos[1])
	mouse.click(Button.left, 1)
	notDone = True

	while notDone:
		try:
			grimmy_ranarr_bank = pyautogui.locateOnScreen('Screenshots/herb/grimmyRanarrBank.png')

			if not grimmy_ranarr_bank:
				notDone = False
				pass

			pos = clickPos(grimmy_ranarr_bank, 4 , 4)
			realmouse.move_mouse_to(pos[0] , pos[1])
			mouse.click(Button.left, 1)

			pos = clickPos(waterVialBank, 2 , 2)
			realmouse.move_mouse_to(pos[0] , pos[1])
			mouse.click(Button.left, 1)

			pos = clickPos(close_bank, 4 , 4)
			realmouse.move_mouse_to(pos[0] , pos[1])
			mouse.click(Button.left, 1)
			# time.sleep(1)

			if not grimmy_ranarr_inv and not waterVialInv:
				grimmy_ranarr_inv = list(pyautogui.locateAllOnScreen('Screenshots/herb/grimmyRanarrInv.png', confidence = .90))
				waterVialInv = list(pyautogui.locateAllOnScreen('Screenshots/herb/waterVialInv.png', confidence = .90))
				
			for i in range(len(grimmy_ranarr_inv)):
				pos = clickPos(grimmy_ranarr_inv[i], 4 , 4)
				realmouse.move_mouse_to(pos[0] , pos[1])
				mouse.click(Button.left, 1)

			ranarr = grimmy_ranarr_inv[-1]
			vial = waterVialInv[0]

			pos = clickPos(vial, 4 , 4)
			realmouse.move_mouse_to(pos[0] , pos[1])
			mouse.click(Button.left, 1)
			
			pos = clickPos(ranarr, 4 , 4)
			realmouse.move_mouse_to(pos[0] , pos[1])
			mouse.click(Button.left, 1)
			
			if (random.choice(['click' , 'space' , 0 , 0])) == 'space':
				time.sleep(.075 * random.randrange(10, 21))
				keyboard.press(' ')
				keyboard.release(' ')
			else:
				time.sleep(.075 * random.randrange(10, 21))
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
		except:
			pass
	try:
		closeBank()
	except:
		pass
	if type == "consumer":
		dummyClick()
		muleRanarrs(Xone, Yone)
	else:
		altmalt_traded = False
		# ihaulstuff_traded = False
		while  altmalt_traded == False:# or ihaulstuff_traded == False:
			altmalt_traderequest = pyautogui.locateOnScreen('Screenshots/trade/altmalt.png', confidence = .90)
			ihaulstuff_traderequest = pyautogui.locateOnScreen('Screenshots/trade/ihaulstuff.png', confidence = .90)
			print("here")
			if altmalt_traderequest and altmalt_traded == False:
				altmalt_traded = True
				alchThread = False
				time.sleep(10)
				acceptSupplies(altmalt_traderequest)

			if ihaulstuff_traderequest and ihaulstuff_traded == False:
				ihaulstuff_traded = True
				time.sleep(10)
				alchThread = False
				acceptSupplies(ihaulstuff_traderequest)
	logOut()

def dummyClick():
	inv = pyautogui.locateOnScreen('Screenshots/misc/openInv.png', confidence = .80)
	pos = clickPos(inv, 4 , 4)
	realmouse.move_mouse_to(pos[0] , pos[1])
	mouse.click(Button.left, 1)

def closeBank():
	close_bank = pyautogui.locateOnScreen('Screenshots/cooking/closeBank.png', confidence = .80)
	pos = clickPos(close_bank, 4 , 4)
	realmouse.move_mouse_to(pos[0] , pos[1])
	mouse.click(Button.left, 1)

def openTradeTab():
	trade_tab = pyautogui.locateOnScreen('Screenshots/trade/tab.png', confidence = .80)
	pos = clickPos(trade_tab, 4 , 4)
	realmouse.move_mouse_to(pos[0] , pos[1])
	mouse.click(Button.left, 1)

def muleRanarrs(Xone, Yone):
	x1 , y1 = stringCord(Xone , Yone)
	realmouse.move_mouse_to(x1 , y1)
	mouse.click(Button.left, 1)
	time.sleep(3)

	note = pyautogui.locateOnScreen('Screenshots/bank/note.png', confidence = .80)
	pos = clickPos(note, 2 , 2)
	realmouse.move_mouse_to(pos[0] , pos[1])
	mouse.click(Button.left, 1)

	quantity = pyautogui.locateOnScreen('Screenshots/bank/all.png', confidence = .80)
	pos = clickPos(quantity, 2 , 2)
	realmouse.move_mouse_to(pos[0] , pos[1])
	mouse.click(Button.left, 1)

	potions = pyautogui.locateOnScreen('Screenshots/herb/ranarrPotion.png', confidence = .95)
	pos = clickPos(potions, 2 , 2)
	realmouse.move_mouse_to(pos[0] , pos[1])
	mouse.click(Button.left, 1)

	closeBank()
	openTradeTab()

	trade_request = pyautogui.locateOnScreen('Screenshots/trade/initiateTrade.png', confidence = .90)
	while not trade_request:
		trade_request = pyautogui.locateOnScreen('Screenshots/trade/initiateTrade.png', confidence = .90)
		print("waiting for trade request to be sent")
	
	pos = clickPos(trade_request, 4 , 2)
	realmouse.move_mouse_to(pos[0] , pos[1])
	mouse.click(Button.left, 1)
	time.sleep(2)

	accept = pyautogui.locateOnScreen('Screenshots/trade/accept.png', confidence = .90)
	while not accept:
		time.sleep(5)
		trade_request = pyautogui.locateOnScreen('Screenshots/trade/initiateTrade.png', confidence = .90)
		pos = clickPos(trade_request, 4 , 2)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)
		accept = pyautogui.locateOnScreen('Screenshots/trade/accept.png', confidence = .90)


	potions = pyautogui.locateOnScreen('Screenshots/herb/ranarrPotionNoted.png', confidence = .95)
	pos = clickPos(potions, 2 , 2)
	realmouse.move_mouse_to(pos[0] , pos[1])
	mouse.click(Button.right, 1)

	time.sleep(2)
	offer_all = pyautogui.locateOnScreen('Screenshots/trade/offer_all.png', confidence = .90)
	pos = clickPos(offer_all, 2 , 2)
	realmouse.move_mouse_to(pos[0] , pos[1])
	mouse.click(Button.left, 1)

	
	accept = pyautogui.locateOnScreen('Screenshots/trade/accept.png', confidence = .90)
	pos = clickPos(accept, 4 , 4)
	realmouse.move_mouse_to(pos[0] , pos[1])
	mouse.click(Button.left, 1)
	time.sleep(1 + .0001 * random.randrange(1, 500))

	secondMenu = pyautogui.locateOnScreen('Screenshots/trade/secondMenu.png', confidence = .90)
	while not secondMenu:
		secondMenu = pyautogui.locateOnScreen('Screenshots/trade/secondMenu.png', confidence = .90)
		print("waiting for other player to accept")

	time.sleep(2)
	accept = pyautogui.locateOnScreen('Screenshots/trade/accept.png', confidence = .90)
	pos = clickPos(accept, 4 , 4)
	realmouse.move_mouse_to(pos[0] , pos[1])
	mouse.click(Button.left, 1)
	time.sleep(1 + .0001 * random.randrange(1, 500))

	while accept:
		accept = pyautogui.locateOnScreen('Screenshots/trade/accept.png', confidence = .90)

def alch():
	#open mage book
	try:
		magebookRed = pyautogui.locateOnScreen('Screenshots/alch/magebookRed.png', confidence = .90)
		if not magebookRed:
			magebook = pyautogui.locateOnScreen('Screenshots/alch/magebook.png', confidence = .90)
			pos = clickPos(magebook, 4 , 4)
			realmouse.move_mouse_to(pos[0] , pos[1])
			mouse.click(Button.left, 1)
			time.sleep(1)
		#cast
		spell = pyautogui.locateOnScreen('Screenshots/alch/spell.png', confidence = .90)
		realmouse.move_mouse_to(random.randrange(spell[0],spell[0] + 5) , random.randrange(spell[1],spell[1] + 5))


		while alchThread:
			magebookRed = pyautogui.locateOnScreen('Screenshots/alch/magebookRed.png', confidence = .90)
			while not magebookRed:
				magebookRed = pyautogui.locateOnScreen('Screenshots/alch/magebookRed.png', confidence = .90)
				print("sleeping")

			mouse.click(Button.left, 1)
			time.sleep(random.randrange(100, 500) * .001)
			mouse.click(Button.left, 1)
	except:
		logOut()

def alchThread():
	t = Thread(target=alch)
	t.daemon = True
	t.start()


def alchNmule():
	altmalt_traded = False
	ihaulstuff_traded = False
	global alchThread
	# alchThread = False

	alchThread()

	while  altmalt_traded == False or ihaulstuff_traded == False:
		altmalt_traderequest = pyautogui.locateOnScreen('Screenshots/trade/altmalt.png', confidence = .90)
		ihaulstuff_traderequest = pyautogui.locateOnScreen('Screenshots/trade/ihaulstuff.png', confidence = .90)
		print("here")
		if altmalt_traderequest and altmalt_traded == False:
			altmalt_traded = True
			alchThread = False
			time.sleep(10)
			acceptSupplies(altmalt_traderequest)

		if ihaulstuff_traderequest and ihaulstuff_traded == False:
			ihaulstuff_traded = True
			time.sleep(10)
			alchThread = False
			acceptSupplies(ihaulstuff_traderequest)
	logOut()

def main():
	script = input("Please Enter which script you would like to run: ")
	if script == 'help':
		print("alch")
		print("arrowshaft")
		print("canifis")
		print("cannon")
		print("cannonBall")
		print("chop")
		print("cooking")
		print("fire")
		print("flax")
		print("flyFish")
		print("gem")
		print("hotWater")
		print("minecoal")
		print("mining")
		print("nmz")
		print("pizza")
		print("ranarrPotion")
		print("sandCrabs")
		print("string")
		print("trainMagic")
		print("varrockAgility")
	elif script == 'sandCrabs':
		sandCrabs()
	elif script == 'minecoal':
		minecoal()
	elif script == 'trainMagic':
		trainMagic()
	elif script == 'hotWater':
		hotWater()
	elif script == 'string':
		string()
	elif script == 'cooking':
		cooking('shark')
	elif script == 'mining':
		skillcheck('mining')
	elif script == 'cannonBall':
		cannonBall()
	elif script == 'arrowshaft':
		arrowshaft()
	elif script == 'pizza':
		pizza()
	elif script == 'ranarrPotion':
		ranarrPotion()
	elif script == 'fire':
		fireMaking()
	elif script == 'varrockAgility':
		varrockAgility()
	elif script == 'canifis':
		canifisAgility()
	elif script == 'nmz':
		nmz()
	elif script == 'alch':
		alch()
	elif script == 'cannon':
		cannon()
	elif script == 'chop':
		treecutting()
	elif script == 'gem':
		gem()
	elif script == 'flyFish':
		flyFish()
	elif script == 'flax':
		spinFlax()
	elif script == 'herbP':
		AIOHerbs("provider")
	elif script == 'herb':
		AIOHerbs("consumer")
	elif script == 'accept':
		acceptSupplies()
	elif script == 'alchNmule':
		alchNmule()
	else:
		print("Invalid script entered. Please enter 'help' for a list of commands")
main()
	

