"""MovementController: Implements various movement methods."""
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
from Custom_Modules import realmouse
from threading import Thread

import webbrowser
import time
import random
import pyautogui


class MovementController():
    """A controller that implements various movement functions via image recognition.""" 
    
    def __init__(self,PixelConversion=1):
        """Init a MovementController instance.
        
        Keyword Arguments:
        PixelConversion -- 1 for PC, 2 for Retina Display
        """
        self.pixelConversion = PixelConversion
        self.keyboard = KeyboardController()
        self.mouse = MouseController()

    def induceError(self, coordinates:str, errorX=5, errorY=5):
        """Induce random error on a coordinate pair.
        
        Keyword argumetns:
        coordinates -- the (x,y) pixel location
        errorX -- error range for x (default 5)
        errorY -- error range for y (default 5)
        """
        return (random.randrange(coordinates[0] - errorX, coordinates[0] + errorX) , random.randrange(coordinates[1] - errorY, coordinates[1]+errorY))


    def moveToCenter(self, primaryImagePath:str, confidenceLevel=.7, waitTime=0):
        """Move to the center of an image on the screen.
        
        Keyword arguments:
        primaryImagePath -- relative path of image to query
        confidenceLevel -- confidence level for image recognition (default .95)
        waitTime -- time to wait after click (default 0)
        """
        location1 = pyautogui.locateCenterOnScreen(
            primaryImagePath, confidence=confidenceLevel)
        while not location1:
            location1 = pyautogui.locateCenterOnScreen(
                primaryImagePath, confidence=.5)
        print('Located')
        pos = self.induceError(location1)
        realmouse.move_mouse_to(pos[0]/self.pixelConversion, pos[1]/self.pixelConversion)
        print("Moved")
        self.mouse.click(Button.left,1)
        time.sleep(waitTime)


   
    def locateAndMoveToCenter(self, primaryImagePath:str, secondaryImagePath:str, confidenceLevel=.95, waitTime=0,checkForMarks=False) -> None:
        """Move to one of two images on the screen.
        
        Keyword arguments:
        primaryImagePath -- relative path of primary image to query
        secondaryImagePath -- relative path of secondary image to query
        confidenceLevel -- confidence level for image recognition (default .95)
        waitTime -- time to wait after click (default 0)
        checkForMarks -- whether or not to query a Mark of Grace on the ground (default False)
        """
        if checkForMarks:
            self.moveToCenter('MarkOfGraceFilePath')
        location1 = pyautogui.locateCenterOnScreen(
            primaryImagePath, confidence=confidenceLevel)
        location2 = pyautogui.locateCenterOnScreen(
            secondaryImagePath, confidence=confidenceLevel)

        while not location1 and location2 and confidenceLevel > 0:
            location1 = pyautogui.locateCenterOnScreen(
                primaryImagePath, confidence=confidenceLevel)
            location2 = pyautogui.locateCenterOnScreen(
                secondaryImagePath, confidence=confidenceLevel)
            confidenceLevel -= .05

        if location1:
            pos = self.induceError(location1, 10, 7)
        else:
            pos = self.induceError(location2, 10 , 7)
        
        realmouse.move_mouse_to(pos[0]/self.pixelConversion, pos[1]/self.pixelConversion)
        self.mouse.click(Button.left, 1)
        time.sleep(waitTime)

