from tkinter import *
from datetime import datetime
import time
from bs4 import BeautifulSoup
import requests

def findLotto():
    url = f"https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={ent.get()}"
    req = requests.get(url)




win = Tk() # 창 생성

# win 옵션
win.geometry("1000x500") # win 크기
win.title("캔디생성!!!!") # win 제목
win.option_add("*Font", "D2Coding 25") #폰트설정
win.geometry("+140+110") # win 시작위치 설정

ent = Entry(win)
ent.get()
ent.pack()

btn = Button()
btn.config(text="로또당첨번호확인")
btn.config(command=findLotto)
btn.pack()

win.mainloop() # 창 실행
