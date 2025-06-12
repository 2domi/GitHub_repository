print("uploading modules...")
import requests
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&page=1"
# url = "https://www.naver.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
}

print("connecting...")
res = requests.get(url, headers=headers)
res.raise_for_status()
print(f"Successfully Connected! | code : {res.status_code}")

soup = BeautifulSoup(res.text, "lxml")

print("scraping...")

items = soup.find_all("li", attrs={"class": "ProductUnit_productUnit__Qd6sv"})
print(items[0].find("div", attrs={"class":"ProductUnit_productName__gre7e"}).get_text())