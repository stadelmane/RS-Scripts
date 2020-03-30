from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
from Custom_Modules import realmouse

import webbrowser
import time
import random
import pyautogui

def logOut():
	mouse = MouseController()

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

def test():
	keyboard = KeyboardController()
	mouse = MouseController()
	keyboard.press(' ')
	keyboard.release(' ')

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
'''
def cooking(food):
	keyboard = KeyboardController()
	mouse = MouseController()
	failures = 0

	itterations = input("Enter how many itterations: ")

	for i in range(int(itterations)):
		
		fire = pyautogui.locateOnScreen('Screenshots/cooking/fire.png', confidence = .80)
		while not fire:
			fire = pyautogui.locateOnScreen('Screenshots/cooking/fire.png', confidence = .80)
			failures += 1
			if failures > 10:
				logout()

		fish = list(pyautogui.locateAllOnScreen('Screenshots/cooking/' + food + 'Inv.png', confidence = .95))
		pos = clickPos(fish[0] , 2 , 4)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)

		
		failures = 0
		pos = clickPos(fire, 4 , 10)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)

		time.sleep(3)
		keyboard.press('1')
		keyboard.release('1')

		lvlUp = pyautogui.locateOnScreen('Screenshots/lvlUp.png', confidence = .80)
		while fish and not lvlUp:
			fish = list(pyautogui.locateAllOnScreen('Screenshots/cooking/' + food + 'Inv.png', confidence = .95))
			lvlUp = pyautogui.locateOnScreen('Screenshots/lvlUp.png', confidence = .80)

		if lvlUp:
			logOut()

		bank = pyautogui.locateOnScreen('Screenshots/cooking/bank.png', confidence = .80)
		pos = clickPos(bank, 3 , 5)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)


		time.sleep(5)
		emptyInv = pyautogui.locateOnScreen('Screenshots/cooking/emptyInv.png', confidence = .95)
		pos = clickPos(emptyInv, 3 , 5)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)

		fish = list(pyautogui.locateAllOnScreen('Screenshots/cooking/' + food + 'Bank.png', confidence = .95))
		pos = clickPos(fish, 3 , 5)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)

		closeBank = pyautogui.locateOnScreen('Screenshots/cooking/closeBank.png', confidence = .80)
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
		sleepTime = random.randrange(54, 61)
		for x in range(0, sleepTime):
			print(sleepTime - x)
			time.sleep(10)

		step1 = pyautogui.locateOnScreen('Screenshots/sandCrabs/step1.png', confidence = .80)
		while not step1:
			step1 = pyautogui.locateOnScreen('Screenshots/sandCrabs/step1.png', confidence = .80)
		pos = clickPos(step1, 3 , 5)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)
		time.sleep(5)

		step2 = pyautogui.locateOnScreen('Screenshots/sandCrabs/step2.png', confidence = .80)
		while not step2:
			step2 = pyautogui.locateOnScreen('Screenshots/sandCrabs/step2.png', confidence = .80)
			print('step2')
		step2 = [step2[0] , step2[1] , int(step2[2] * .3) , step2[3]]
		pos = clickPos(step2, 0 , 8)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)
		time.sleep(6)

		farthestPoint = pyautogui.locateOnScreen('Screenshots/sandCrabs/farthestPoint.png', confidence = .80)
		while not farthestPoint:
			farthestPoint = pyautogui.locateOnScreen('Screenshots/sandCrabs/farthestPoint.png', confidence = .80)
			print('farthestPoint')
		pos = clickPos(farthestPoint, 10 , 7)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)
		time.sleep(5)

		#begin run back
		step3 = pyautogui.locateOnScreen('Screenshots/sandCrabs/step3.png', confidence = .8)
		stepThree = pyautogui.locateOnScreen('Screenshots/sandCrabs/stepThree.png', confidence = .8)
		while not step3 and not stepThree:
			print('step3')
			step3 = pyautogui.locateOnScreen('Screenshots/sandCrabs/step3.png', confidence = .7)
			stepThree = pyautogui.locateOnScreen('Screenshots/sandCrabs/stepThree.png', confidence = .7)
		if step3:
			pos = clickPos(step3, 6 , 10)
		else:
			pos = clickPos(stepThree, 3 , 5)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)
		time.sleep(3.5)

		step4 = pyautogui.locateOnScreen('Screenshots/sandCrabs/step4.png', confidence = .80)
		while not step4:
			step4 = pyautogui.locateOnScreen('Screenshots/sandCrabs/step4.png', confidence = .80)
			print('step4')
		pos = clickPos(step4, 6 , 10)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)
		time.sleep(3.5)

		step5 = pyautogui.locateOnScreen('Screenshots/sandCrabs/step5.png', confidence = .80)
		while not step5:
			step5 = pyautogui.locateOnScreen('Screenshots/sandCrabs/step5.png', confidence = .80)
		pos = clickPos(step5, 6 , 6)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)
		time.sleep(5)

		step6 = pyautogui.locateOnScreen('Screenshots/sandCrabs/step6.png', confidence = .80)
		while not step6:
			step6 = pyautogui.locateOnScreen('Screenshots/sandCrabs/step6.png', confidence = .80)
		pos = clickPos(step6, 6 , 6)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)
		time.sleep(5)

		destination = pyautogui.locateOnScreen('Screenshots/sandCrabs/destination.png', confidence = .70)
		while not destination:
			destination = pyautogui.locateOnScreen('Screenshots/sandCrabs/destination.png', confidence = .70)
		pos = clickPos(destination, 5 , 5)
		realmouse.move_mouse_to(pos[0] , pos[1])
		mouse.click(Button.left, 1)


def main():
	# sandCrabs()
	# minecoal()
	# string()
	# test()
	# cooking('tuna')
	# skillcheck('mining')
	cannonBall()
	# arrowshaft()
	logOut()
	# train()

main()


	

