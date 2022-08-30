import time

import pyautogui


IS_SHOPPING_MODE = True


pyautogui.mouseInfo()
time.sleep(2)
iteration = 0

while True:
    iteration += 1
    if iteration == 10:
        iteration = 0
        retry_icon = pyautogui.locateOnScreen('resources/Retry.png', confidence=0.7, region=(1100, 800, 300, 100))
        if retry_icon:
            # Click retry
            pyautogui.click(1250, 850)
            time.sleep(15)
        # Click continue
        continue_screen = pyautogui.locateOnScreen('resources/tap_to_continue_screen.png', confidence=0.7)
        if continue_screen:
            pyautogui.click(1000, 1000)
            pyautogui.click(1000, 1000)
            pyautogui.click(1000, 1000)
            pyautogui.doubleClick(1000, 1000)
            pyautogui.doubleClick(1000, 1000)
            pyautogui.doubleClick(1000, 1000)

        def mission_finished():
            return pyautogui.locateCenterOnScreen('resources/Collect.png',
                                                  confidence=0.7,
                                                  grayscale=True,
                                                  region=(1100, 750, 300, 300))

        def final_goal_complete():
            return pyautogui.locateCenterOnScreen('resources/ok.png',
                                                  confidence=0.7,
                                                  grayscale=True,
                                                  region=(1100, 750, 300, 300))

        has_finished = mission_finished()
        if has_finished:
            x, y = has_finished
            pyautogui.click(x, y)
        else:
            has_finished = final_goal_complete()
            if has_finished:
                x, y = has_finished
                pyautogui.click(x, y)

    # Check for new quest
    exclamation_mark = pyautogui.locateCenterOnScreen('resources/ExclamationMark.png', confidence=0.7,
                                                      region=(0, 0, 400, 400))
    if exclamation_mark:
        pyautogui.click(*exclamation_mark)
        continue

    # Check if someone finished their task
    v_mark = pyautogui.locateCenterOnScreen('resources/V Mark.png', confidence=0.7, region=(0, 0, 400, 400))
    if v_mark:
        x, y = v_mark
        # Click "V"
        pyautogui.click(x, y + 15)
        # Collect money from task
        pyautogui.click(1250, 450)

    # Check for open shop
    heights_icon = pyautogui.locateOnScreen('resources/SpringfieldHeights.png', confidence=0.6, region=(1450, 100, 300, 120))
    if heights_icon:
        furniture_icon = pyautogui.locateOnScreen('resources/FurnitureIcon.png', confidence=0.6, region=(1600, 300, 150, 100))
        coffee_icon = pyautogui.locateOnScreen('resources/CoffeeIcon.png', confidence=0.6, region=(1600, 300, 150, 100))
        electronic_icon = pyautogui.locateOnScreen('resources/electronic.png', confidence=0.6, region=(1600, 300, 150, 100))
        yoga_icon = pyautogui.locateOnScreen('resources/YogaShop.png', confidence=0.6, region=(1600, 300, 150, 100))
        if furniture_icon or coffee_icon or electronic_icon or yoga_icon:
            if IS_SHOPPING_MODE and (furniture_icon or coffee_icon or yoga_icon):
                def find_button():
                    return pyautogui.locateCenterOnScreen('resources/StartTask.png', confidence=0.85,
                                                          region=(1400, 300, 500, 800),
                                                          grayscale=True)


                button = find_button()
                while button:
                    pyautogui.click(*button)
                    button = find_button()
        # Close shop
        close_sign = pyautogui.locateCenterOnScreen('resources/CloseModal.png', confidence=0.6, region=(450, 200, 350, 100))
        if close_sign:
            pyautogui.click(*close_sign)
            continue

    # Check for available task
    search_mark = pyautogui.locateCenterOnScreen('resources/search.png', confidence=0.7, region=(0, 0, 400, 400))
    if search_mark:
        x, y = search_mark
        pyautogui.click(x, y)

        if IS_SHOPPING_MODE:
            # time.sleep(0.01)
            pyautogui.click(x, y)

        # Start "Buy Old Film Reels" task
        film_task = None
        for _ in range(3):
            film_task = pyautogui.locateOnScreen('resources/FilmTask.png',
                                                 confidence=0.8,
                                                 region=(840, 220, 1250, 800),
                                                 grayscale=True)
            if film_task:
                start_button = pyautogui.locateCenterOnScreen('resources/StartTask.png',
                                                              confidence=0.85,
                                                              region=(int(film_task.left + 550),
                                                                      film_task.top - film_task.height,
                                                                      600,
                                                                      film_task.top + film_task.height),
                                                              grayscale=True)
                pyautogui.click(*start_button)
                break

        # Start "60 minutes for 70 bucks" task
        # job_60_70 = None
        # for _ in range(3):
        #     job_60_70 = pyautogui.locateOnScreen('resources/60-70job.png',
        #                                          confidence=0.85,
        #                                          region=(1100, 325, 250, 1075),
        #                                          grayscale=True)
        #
        #     if job_60_70:
        #         start_button = pyautogui.locateCenterOnScreen('resources/StartTask.png',
        #                                                       confidence=0.85,
        #                                                       region=(int(job_60_70.left + 550),
        #                                                               job_60_70.top - job_60_70.height,
        #                                                               350,
        #                                                               job_60_70.top + job_60_70.height),
        #                                                       grayscale=True)
        #         pyautogui.click(*start_button)
        #         break

        # Start "Bump Into a Sad Lonely Homer" task
        bump_task = None
        for _ in range(3):
            bump_task = pyautogui.locateOnScreen('resources/BumpIntoHomer.png',
                                                 confidence=0.85,
                                                 region=(840, 220, 1250, 800),
                                                 grayscale=True)
            if bump_task:
                start_button = pyautogui.locateCenterOnScreen('resources/StartTask.png',
                                                              confidence=0.85,
                                                              region=(int(bump_task.left + (bump_task.width * 2 / 3)),
                                                                      bump_task.top,
                                                                      int(bump_task.width / 3),
                                                                      bump_task.height),
                                                              grayscale=True)
                pyautogui.click(*start_button)
                break
    # Check if "Level" disappeared (assuming currently a mission's dialog is displayed)
    level = pyautogui.locateCenterOnScreen('resources/Level.png',
                                           confidence=0.85,
                                           region=(275, 1175, 110, 50),
                                           grayscale=True)
    if not level:
        pyautogui.click(275, 1175)
