import pyautogui
import pydirectinput
import random
import time
import keyboard

def startLoop():
    coordList = [[518, 572], [986, 579], [1410, 559]]

    for i  in coordList:
        # print(i[0], 'X end')
        # print(i[1], 'Y end')
        time.sleep(random.randint(1, 5)/10)

        pydirectinput.moveTo(i[0], i[0], 0.25) # Move the mouse to the x, y coordinates 100, 150.
        pydirectinput.click() # Click the mouse at its current location.
        # pydirectinput.move(None, 10)

        if keyboard.is_pressed('ctrl+alt+s'):
            break

def getCoordinates():
    current_x, current_y = pyautogui.position()
    print(f"Текущие координаты: X = {current_x}, Y = {current_y}")

keyboard.add_hotkey('ctrl+q', startLoop)
keyboard.add_hotkey('ctrl+alt+d', getCoordinates)

keyboard.wait()
