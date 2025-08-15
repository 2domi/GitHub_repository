import pyautogui
import keyboard
import time

while True:
    if keyboard.is_pressed("1"):
        pyautogui.press("f5")
        end_time = time.time() + 1.6

        while time.time() < end_time:
                pyautogui.click(1212,956)

    if keyboard.is_pressed("2"):
        pyautogui.click(841,366)
        time.sleep(0.1)
        pyautogui.click(443,605)
    
    if keyboard.is_pressed("3"):
        pyautogui.click(751, 284)
        pyautogui.click(745, 371)
        pyautogui.click(755,576)
        pyautogui.click(728,665)
        pyautogui.click(1048,797)
        time.sleep(0.3)
        pyautogui.click(293,506)
        pyautogui.click(538,567)
        pyautogui.click(1048,797)
        
    if keyboard.is_pressed("4"):
        pyautogui.click(751, 284)
        pyautogui.click(751,434)
        pyautogui.click(1048,797)
        time.sleep(0.3)
        pyautogui.click(293,506)
        pyautogui.click(538,567)
        pyautogui.click(1048,797)

import pyautogui
import time

while True:
    time.sleep(0.1)
    print(pyautogui.position())