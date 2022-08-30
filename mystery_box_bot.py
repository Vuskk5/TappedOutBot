import time

import pyautogui

pyautogui.mouseInfo()

while True:
    box = pyautogui.locateCenterOnScreen('resources_3k/mysterybox.png', confidence=0.9)
    if box:
        x, y = box
        pyautogui.click(x, y + 240)
        time.sleep(0.05)
        pyautogui.click(1250, 825)
        time.sleep(0.05)
        pyautogui.click(2370, 1300)
        time.sleep(0.05)

