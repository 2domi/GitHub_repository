import pyautogui
import keyboard
import time

while True:
    if keyboard.is_pressed("`"):
        print(pyautogui.position())
        time.sleep(0.2)