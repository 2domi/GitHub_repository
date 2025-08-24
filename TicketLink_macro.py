import pyautogui
import time
import keyboard

while True:
    if keyboard.is_pressed("1"):
        pyautogui.press("f5") # 새로고침
        
        end_time = time.time() + 1.7 # 3초동안 클릭 반복(예매하기 버튼)
        while end_time > time.time():
            pyautogui.click(1139, 860)
        
        time.sleep(0.3)
        pyautogui.hotkey("ctrl","+") # 창 확대
        pyautogui.hotkey("ctrl","+")
        pyautogui.hotkey("ctrl","+")
        pyautogui.hotkey("ctrl","+")
        pyautogui.hotkey("ctrl","+")

    if keyboard.is_pressed("2"):
        pyautogui.click(451,603) # 캡챠 입력창 바로가기

    if keyboard.is_pressed("3"): # 어른이/어린이
        pyautogui.click(764,578) # 어른이
        pyautogui.click(759,665) # 2매 지정
        pyautogui.click(760,648) # 어린이
        pyautogui.click(762,741) # 2매 지정
        pyautogui.click(1036,949) # 다음으로

        time.sleep(1.5)

        pyautogui.click(63,690) #동의
        pyautogui.click(65,758) #동의
        pyautogui.click(66,806)  #동의
        pyautogui.click(63,865) #동의
        pyautogui.click(865,766) #동의
        pyautogui.click(878,870) # 결제수단 선택
        pyautogui.click(1015,961) # 결제하기

    if keyboard.is_pressed("4"):
        pyautogui.click(764,578) # 어른이
        pyautogui.click(729,728) # 4매
        pyautogui.click(1036,949) # 다음으로

        time.sleep(1.5)

        pyautogui.click(63,713)
        pyautogui.click(64,776)
        pyautogui.click(64,829)
        pyautogui.click(64,882)
        pyautogui.click(64,936)
        pyautogui.click(865,766) #동의
        pyautogui.click(878,870) # 결제수단 선택
        pyautogui.click(1015,961) # 결제하기