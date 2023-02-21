from BaseScript import BaseScript

from Custom_Modules import realmouse
from Custom_Modules import realmouse

import time
import pyautogui
import random
import typing
import time
import random

class MineCoal(BaseScript):
	def pre_check(self):
		# super()
		rock_1 = pyautogui.locateOnScreen('Screenshots/coalMining/rock1.png', confidence = .70)
		rock_2 = pyautogui.locateOnScreen('Screenshots/coalMining/rock2.png', confidence = .70)
		rock_3 = pyautogui.locateOnScreen('Screenshots/coalMining/rock3.png', confidence = .70)
		if rock_1 is None or rock_2 is None or rock_3 is None:
			print("If rock_1 is missing, try tunring on entity hider")
			print(f"rock_1: {rock_1}, rock_2: {rock_2}, rock_3: {rock_3}")
			return False	
		return True

	def run(self):

		sleep_time = 1.3
		inv_count = 0

		rock_1 = pyautogui.locateOnScreen('Screenshots/coalMining/rock1.png', confidence = .70)
		rock_2 = pyautogui.locateOnScreen('Screenshots/coalMining/rock2.png', confidence = .70)
		rock_3 = pyautogui.locateOnScreen('Screenshots/coalMining/rock3.png', confidence = .70)
		itterations = input("How many itterations: ")

		for i in range(int(itterations)):
			if i % 10 == 0:
				print(f"Itteration: {i}")

			curr_count = list(pyautogui.locateAllOnScreen('Screenshots/coalMining/ironoreInv.png', confidence = .90))
			print(len(curr_count), inv_count)
			if inv_count + 3 == len(curr_count):
				sleep_time += -.005
				print(sleep_time)
			else:
				sleep_time += .005
				print("in else statement")
			if self.invFull('ironoreInv' , 'coalMining' , 20):
				self.dropItem('ironoreInv' , 'coalMining')

			inv_count = len(curr_count)

			if random.randrange(0, 100) == 68:
				self.skillcheck('mining')	

			self.move_mouse_and_click(object=rock_1, deviation_x=20, deviation_y=20, sleep_time=sleep_time)
			self.move_mouse_and_click(object=rock_2, deviation_x=20, deviation_y=20, sleep_time=sleep_time)
			self.move_mouse_and_click(object=rock_3, deviation_x=20, deviation_y=20, sleep_time=sleep_time)

if __name__ == '__main__':
	script = MineCoal()
	script.execute()