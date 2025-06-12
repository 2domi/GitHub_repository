import requests as res
from bs4 import BeautifulSoup

# 암튼 실패한거

url = "https://playentry.org/"
site = res.get(url)
site.raise_for_status()

soup = BeautifulSoup(site.text, "lxml")

print("title:", soup.title.get_text())
staff_pick1 = soup.find("li", class_="css-1kqr8os e1cpvx0q1")
staff_pick2 = staff_pick1.find_next_sibling()
staff_pick3 = staff_pick2.find_next_sibling()
staff_pick4 = staff_pick3.find_next_sibling()

print(staff_pick1.a.get_text())
print(staff_pick2.a.get_text())
print(staff_pick3.a.get_text())
print(staff_pick4.a.get_text())

### beautifulsoup4 ###
# soup.title    : soup 객체의 제목
# soup.a        : soup 객체에서 처음 발견되는 a element 반환
# soup.a.get_text : 문자열만 반환
# soup.a.attrs  : soup 객체에서 처음 발견되는 a element의 속성 반환
# soup.a[href]  : soup 객체에서 처음 발견되는 a element의 href 속성 반환
# soup.find("a", attrs={class:Nbtn_upload}) : 처음 발견된 a 태그의 속성이 class=Nbtn_upload인 element 반환