import pyautogui


def skip_to_neighbor():
    collect_exp = pyautogui.locateCenterOnScreen('resources_3k/Collect.png', confidence=0.7, grayscale=True,
                                                 region=(1150, 750, 200, 150))
    if collect_exp:
        # Click "collect" bonus exp for finishing neighbour
        pyautogui.click(*collect_exp)
        # Click to skip to next neighbor
        pyautogui.click(600, 150)


if __name__ == '__main__':
    while True:
        skip_to_neighbor()
