from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
from Custom_Modules import realmouse

import time
import pyautogui
import random
import typing


class BaseScript:
    def __init__(self):
        self.mouse = MouseController()
        self.keyboard = KeyboardController()

    def pre_check(self):
        print(f"Pre-check started at {time.ctime()}")

    def run(self):
        pass

    def post_check(self):
        self.logOut()
        print(f"Post-check finished at {time.ctime()}")

    def execute(self):
        if self.pre_check():
            self.run()
        self.post_check()

    def move_mouse(self, object, deviation_x: int, deviation_y: int, sleep_time: float=None):
        pos = self.clickPos(object, deviation_x , deviation_y)
        realmouse.move_mouse_to(pos[0] , pos[1])

    def move_mouse_and_click(self, object, deviation_x: int, deviation_y: int, sleep_time: float=None):
        pos = self.clickPos(object, deviation_x , deviation_y)
        realmouse.move_mouse_to(pos[0] , pos[1])
        self.mouse.click(Button.left, 1)
        if sleep_time:
            # print(f"sleeping for {sleep_time} seconds")
            time.sleep(sleep_time)

    def clickPos(self, item, errorX, errorY):
        return random.randrange(item[0] + errorX , item[0] + item[2] - errorX) , random.randrange(item[1] + errorY , item[1] + item[3] - errorY)

    def invFull(self, item, folder, quantity):
        invItem = list(pyautogui.locateAllOnScreen('Screenshots/' + folder + '/' + item + '.png', confidence = .70))
        if len(invItem) >= quantity:
            return True
        else:
            return False

    def dropItem(self, item, folder):
        inv = list(pyautogui.locateAllOnScreen('Screenshots/' + folder + '/' + item + '.png', confidence = .90))
        with self.keyboard.pressed(Key.shift):
            for obj in inv:
                self.move_mouse_and_click(object=obj, deviation_x=3, deviation_y=3)
            time.sleep(.2)


    def skillcheck(self, skill):
        skillTab = pyautogui.locateOnScreen('Screenshots/skillcheck/skillTab.png', confidence = .70)
        if skillTab:
            self.move_mouse_and_click(object=skillTab, deviation_x=3, deviation_y=3, sleep_time=.5)
        
        skill = pyautogui.locateOnScreen('Screenshots/skillcheck/' + skill + '.png' , confidence = .70)
        if skill:
            self.move_mouse(object=skill, deviation_x=3, deviation_y=3, sleep_time=(3 + .0001 * random.randrange(1, 500)))
        
        inv = pyautogui.locateOnScreen('Screenshots/skillcheck/inv.png', confidence = .70)
        if inv:
            self.move_mouse_and_click(object=inv, deviation_x=3, deviation_y=3, sleep_time=(3 + .0001 * random.randrange(1, 500)))
        else:
            self.logout()

    def logOut(self):
        logout_menu_button = pyautogui.locateOnScreen('Screenshots/logout/log.png' , confidence = .9)
        if logout_menu_button:
            sleep_time=(1 + .0001 * random.randrange(1, 500))
            self.move_mouse_and_click(object=logout_menu_button, deviation_x=3, deviation_y=3, sleep_time=sleep_time)

        logout_button = pyautogui.locateOnScreen('Screenshots/logout/logout.png' , confidence = .9)
        if logout_button:
            self.move_mouse_and_click(object=logout_button, deviation_x=3, deviation_y=3)