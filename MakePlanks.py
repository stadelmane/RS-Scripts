from BaseScript import BaseScript

from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
from Custom_Modules import realmouse
from Custom_Modules import realmouse

import time
import pyautogui
import random
import typing
import time
import random

class MakePlanks(BaseScript):
	def pre_check(self):
  #   	try:
		print(f"Pre-check started at {time.ctime()}")
	 #    	input('press enter on banker')
		# 	banker = int((mouse.position)[0]), int((mouse.position)[1]), 60, 40
			
		# 	input('press enter when bank tab is opened to begin script')

		# 	withdrawl_all_quantity_btn = pyautogui.locateOnScreen('Screenshots/bank/all.png', confidence = .90)
		# 	close_bank_btn = pyautogui.locateOnScreen('Screenshots/bank/closeBank.png', confidence = .80)
		# 	logs_bank = pyautogui.locateOnScreen('Screenshots/magic/plank/logs_bank.png', confidence = .99)

		# 	try:
		# 		print("Setting withdrawl quantity to all")	
		# 		move_mouse_and_click(object=withdrawl_all_quantity_btn, deviation_x=4, deviation_y=4)

		# 	except:
		# 		print("Couldn't find withdrawl_all_quantity_btn, likely already set")
		# 		pass

		# except:
	 #    	return False
		return True

	def run(self):

		input('press enter on banker')
		banker = int((self.mouse.position)[0]), int((self.mouse.position)[1]), 60, 40		
		input('press enter when bank tab is opened to begin script')

		print(f"Starting MakePlanks: {time.ctime()}")

		close_bank_btn = pyautogui.locateOnScreen('Screenshots/bank/closeBank.png', confidence = .80)
		logs_bank = pyautogui.locateOnScreen('Screenshots/magic/plank/logs_bank.png', confidence = .99)
		finished = False
		while not finished:
			try:
				print("clicking logs_bank", logs_bank)
				self.move_mouse_and_click(logs_bank, deviation_x=4, deviation_y=4)

				print("clicking close bank btn")
				self.move_mouse_and_click(object=close_bank_btn, deviation_x=4, deviation_y=4, sleep_time=.2)


				spell_book = pyautogui.locateOnScreen('Screenshots/magic/plank/spell_book.png', confidence = .99)
				if spell_book:
					print("Opening spell book")
					self.move_mouse_and_click(object=spell_book, deviation_x=4, deviation_y=4, sleep_time=2)

				plank_spell = pyautogui.locateOnScreen('Screenshots/magic/plank/plank_spell.png', confidence = .85)
				print("casting spell")
				self.move_mouse_and_click(object=plank_spell, deviation_x=4, deviation_y=4, sleep_time=1)

				logs = list(pyautogui.locateAllOnScreen('Screenshots/magic/plank/logs_inv.png', confidence = .90))
				self.move_mouse_and_click(object=logs[-1], deviation_x=4, deviation_y=4, sleep_time=.5)				
				logs.pop()

				method = random.choice([1, 1, 1, 2, 2])
				print(f"method: {method}")
				if method == 2:
					time.sleep(90)
				else:
					for log in logs:
						self.move_mouse_and_click(object=plank_spell, deviation_x=4, deviation_y=4, sleep_time=.2)
						self.move_mouse_and_click(object=log, deviation_x=4, deviation_y=4, sleep_time=.5)
				
				print("click banker")
				self.move_mouse_and_click(object=banker, deviation_x=10, deviation_y=15, sleep_time=1)

				print("click empty inv")
				planks = list(pyautogui.locateAllOnScreen('Screenshots/magic/plank/plank_inv2.png', confidence = .85))
				self.move_mouse_and_click(object=planks[-5], deviation_x=4, deviation_y=4)

			except Exception as e:
				x = input('End script? hit 1 to continue 2 to end')
				if x == '2':
					finished=True 
				print(e)
				# print(traceback.format_exc())

if __name__ == '__main__':
	script = MakePlanks()
	script.execute()