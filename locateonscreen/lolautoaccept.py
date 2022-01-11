import pyautogui
import time

while True:
    try:
        x, y = pyautogui.locateCenterOnScreen('accept.png')
        pyautogui.moveTo(x, y)
        pyautogui.click(x, y)
    except:
        time.sleep(0.1)
