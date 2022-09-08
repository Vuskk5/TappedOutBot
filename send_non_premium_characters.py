import time

import pyautogui


def send_characters():
    heights_icon = pyautogui.locateOnScreen('resources_3k/SpringfieldHeights.png', confidence=0.6, grayscale=True,
                                            region=(1400, 230, 220, 100))
    if heights_icon:
        close_sign = pyautogui.locateCenterOnScreen('resources_3k/CloseModal.png', confidence=0.6,
                                                    region=(850, 300, 70, 70))
        if close_sign:
            pyautogui.click(*close_sign)

    search_mark = pyautogui.locateCenterOnScreen('resources_3k/SearchMark.png', confidence=0.7,
                                                 region=(75, 50, 175, 150))
    if search_mark:
        pyautogui.click(*search_mark)

        task_35_dollar = pyautogui.locateOnScreen('resources_3k/35$.png', confidence=0.6, grayscale=True,
                                                  region=(940, 400, 1000, 550))
        if task_35_dollar:
            x = task_35_dollar.left + task_35_dollar.width
            y = task_35_dollar.top + task_35_dollar.height
            for _ in range(20):
                pyautogui.moveTo(x, y)
                pyautogui.scroll(-1)
                task_600_dollar = pyautogui.locateOnScreen('resources_3k/600$.png', confidence=0.85, grayscale=True,
                                                           region=(940, 400, 1000, 550))
                if task_600_dollar:
                    start_button = pyautogui.locateCenterOnScreen('resources_3k/StartTask.png', confidence=0.85,
                                                                  grayscale=True,
                                                                  region=(1600,
                                                                          task_600_dollar.top - 150,
                                                                          300,
                                                                          task_600_dollar.height + 150))
                    if start_button:
                        pyautogui.click(*start_button)


if __name__ == '__main__':
    while True:
        send_characters()
        time.sleep(0.5)
