import random
import time

import pyautogui

pyautogui.mouseInfo()

while True:
    box = pyautogui.locateCenterOnScreen('resources_3k/mysterybox.png', confidence=0.9)
    if box:
        x, y = box
        pyautogui.click(x, y + 240)
        time.sleep(random.random())
        pyautogui.click(1250, 825)
        time.sleep(random.random())
        pyautogui.click(2370, 1300)
        time.sleep(random.random())

