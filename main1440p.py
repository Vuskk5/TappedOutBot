import random
import time

import pyautogui


IS_SHOPPING_MODE = False
SHOPPING_SKIPS = 1


pyautogui.mouseInfo()
time.sleep(2)
iteration = 0

while True:
    iteration += 1
    if iteration == 20:
        iteration = 0

        # Level up
        gift = pyautogui.locateCenterOnScreen('resources_3k/Gift.png', confidence=0.7, region=(800, 250, 1000, 750))
        if gift:
            pyautogui.click(*gift)
            time.sleep(5)
            collect = pyautogui.locateCenterOnScreen('resources_3k/Collect.png', confidence=0.7, grayscale=True,
                                                     region=(1400, 680, 200, 200))
            pyautogui.click(*collect)

        # Click retry
        retry_icon = pyautogui.locateCenterOnScreen('resources_3k/Retry.png', confidence=0.7, region=(1150, 750, 200, 100))
        if retry_icon:
            pyautogui.click(*retry_icon)
            time.sleep(15)
        # Click continue
        continue_screen = pyautogui.locateOnScreen('resources_3k/TapToContinue.png', confidence=0.7, grayscale=True,
                                                   region=(2000, 1300, 500, 100))
        if continue_screen:
            pyautogui.click(1000, 1000)
            pyautogui.click(1000, 1000)
            pyautogui.click(1000, 1000)
            pyautogui.doubleClick(1000, 1000)
            pyautogui.doubleClick(1000, 1000)
            pyautogui.doubleClick(1000, 1000)

        # Check if quest finish modal has popped-up
        quest_finished = pyautogui.locateCenterOnScreen('resources_3k/Collect.png', confidence=0.7, grayscale=True,
                                                        region=(1150, 750, 200, 100))
        if quest_finished:
            pyautogui.click(*quest_finished)

        # Check if final task of quest chain has been completed
        chain_finished = pyautogui.locateCenterOnScreen('resources_3k/Ok.png', confidence=0.7, grayscale=True,
                                                        region=(1150, 750, 200, 200))
        if chain_finished:
            pyautogui.click(*chain_finished)

    # Check for new quest
    exclamation_mark = pyautogui.locateCenterOnScreen('resources_3k/ExclamationMark.png', confidence=0.7,
                                                      region=(75, 50, 175, 150))
    if exclamation_mark:
        pyautogui.click(*exclamation_mark)
        continue

    # Check if someone finished their task
    v_mark = pyautogui.locateCenterOnScreen('resources_3k/CheckMark.png', confidence=0.7, region=(75, 50, 175, 150))
    if v_mark:
        x, y = v_mark
        # Click "V"
        pyautogui.click(x, y + 15)
        # Collect money from task
        pyautogui.click(1250, 550)

    # Check for open shop
    heights_icon = pyautogui.locateOnScreen('resources_3k/SpringfieldHeights.png', confidence=0.6, grayscale=True,
                                            region=(1400, 230, 220, 100))
    if heights_icon:
        if IS_SHOPPING_MODE:
            shop_locator_data = {
                'confidence': 0.6,
                'grayscale': True,
                'region': (1550, 350, 100, 70)
            }

            # Contains the names of all image names
            heights_facilities = ['HeightsFurniture', 'HeightsCoffee', 'HeightsYoga', 'Pill', 'Trophy']

            for facility in heights_facilities:
                facility_icon = pyautogui.locateOnScreen(f'resources_3k/{facility}.png', **shop_locator_data)

                if facility_icon:
                    def find_start_task_button():
                        return pyautogui.locateCenterOnScreen('resources_3k/StartTask.png', confidence=0.85,
                                                              region=(1500, 410, 400, 540))


                    button = find_start_task_button()
                    while button:
                        pyautogui.click(*button)
                        button = find_start_task_button()
                    break

        # Close shop
        close_sign = pyautogui.locateCenterOnScreen('resources_3k/CloseModal.png', confidence=0.6, region=(850, 300, 70, 70))
        if close_sign:
            pyautogui.click(*close_sign)
            continue

    # Check for available task
    search_mark = pyautogui.locateCenterOnScreen('resources_3k/SearchMark.png', confidence=0.7, region=(75, 50, 175, 150))
    if search_mark:
        x, y = search_mark
        pyautogui.click(x, y)

        if IS_SHOPPING_MODE:
            # This skips 1 character, essentially allowing us to reach the shops on some occasions
            for _ in range(SHOPPING_SKIPS):
                pyautogui.click(x, y)

        bump_task = None
        event_task = None
        for _ in range(3):
            # Start "LookForToyRayGuns" task
            event_task = pyautogui.locateOnScreen('resources_3k/LookForToyRayGuns.png', confidence=0.8, grayscale=True,
                                                  region=(940, 400, 1000, 550))
            if event_task:
                start_button = pyautogui.locateCenterOnScreen('resources_3k/StartTask.png', confidence=0.85,
                                                              grayscale=True,
                                                              region=(1600,
                                                                      event_task.top,
                                                                      300,
                                                                      event_task.top + event_task.height))
                pyautogui.click(*start_button)
                break

            # Start "Bump Into a Sad Lonely Homer" task
            bump_task = pyautogui.locateOnScreen('resources_3k/BumpIntoHomer.png', confidence=0.85, grayscale=True,
                                                 region=(940, 400, 1000, 550))
            if bump_task:
                start_button = pyautogui.locateCenterOnScreen('resources_3k/StartTask.png', confidence=0.85,
                                                              grayscale=True,
                                                              region=(1600,
                                                                      bump_task.top,
                                                                      300,
                                                                      bump_task.height))
                pyautogui.click(*start_button)
                break
    # Check if "Level" disappeared (assuming currently a mission's dialog is displayed)
    level = pyautogui.locateCenterOnScreen('resources_3k/UserLevel.png', confidence=0.85, grayscale=True,
                                           region=(200, 1220, 120, 40))
    if not level:
        pyautogui.click(270, 1240)
