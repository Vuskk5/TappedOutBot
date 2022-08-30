import time

import pyautogui


FIRST_BOX, SECOND_BOX, THIRD_BOX = range(3)
STATE = FIRST_BOX


def donut_boxes():
    level_up_box = pyautogui.locateCenterOnScreen('resources_3k/BonusLevelUpBox.png', confidence=0.7, grayscale=True,
                                                  region=(1150, 450, 200, 200))
    if level_up_box:
        pyautogui.click(*level_up_box)
        time.sleep(2.5)

    def find_another_box(x, w):
        return pyautogui.locateCenterOnScreen('resources_3k/OpenAnotherLevelUpBox.png', confidence=0.7, grayscale=True,
                                              region=(x, 620, w, 60))

    # If two donuts, start on right side
    two_donuts = pyautogui.locateCenterOnScreen('resources_3k/TwoDonuts.png', confidence=0.9, grayscale=True,
                                                region=(1150, 450, 200, 200))
    if two_donuts:
        another_box = find_another_box(950, 300)
    else:
        another_box = find_another_box(1250, 300)

    while another_box:
        pyautogui.click(*another_box)
        time.sleep(2.5)
        another_box = find_another_box(950, 600)

    collect = pyautogui.locateCenterOnScreen('resources_3k/Collect.png', confidence=0.7, grayscale=True,
                                             region=(1400, 680, 200, 100))
    if collect:
        pyautogui.click(*collect)


if __name__ == '__main__':
    while True:
        donut_boxes()
