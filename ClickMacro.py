import keyboard
import sys
import time
import pydirectinput

pydirectinput.PAUSE = 0

AutoClick = False

print("[실행]")
while True:
    if AutoClick:
          pydirectinput.click()


    if keyboard.is_pressed("scroll lock"):
        AutoClick = not AutoClick
        time.sleep(0.1)
        print(f"<AutoClick: {AutoClick}>")


    if keyboard.is_pressed("q") and keyboard.is_pressed("ctrl"):
        print("[종료]")
        sys.exit()

    else:
        while keyboard.is_pressed("`"):
            pydirectinput.click()