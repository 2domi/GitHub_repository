print("uploading modules...")
import requests
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&page=1"

# 헤더 지정
headers = {
    "authority": "www.coupang.com",
    "method": "GET",
    "path": "/",
    "scheme": "https",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "max-age=0",
    "cookie": (
        "PCID=17497311077329811692943; x-coupang-target-market=KR; x-coupang-accept-language=ko-KR; "
        "sid=426c6881a44a4f83be54098ae0d6ff92e5494087; searchKeyword=%EB%85%B8%ED%8A%B8%EB%B6%81; "
        "searchKeywordType={%22%EB%85%B8%ED%8A%B8%EB%B6%81%22:0}; MARKETID=17497311077329811692943; "
        "overrideAbTestGroup=%5B%5D; bm_ss=ab8e18ef4e; _abck=056DAB9DF6F7ACC18632437471FACDF4~0~YAAQTNojF5SpUWmXAQAAaSAFbg5xfWjazbMxpBoM/YyfU2lLnyvjXKgy/nvI7Wu2RBJ1IOW3o77ts/oZNUv7Lfhc8waHMKYhao93byiDzN1tNrRfoizTUeTf5UXx+d+RIZmU7YtL5P7G3SyxhzQDGJzTZEsTtc+Vnh4VGSH/MPdL/I4heH5lU9F7SLaS+kJgLsOeknnCxsM7awePO+o0ppXJYq3Gv3Je7S++VIqekUMclxQ5REov1ApF9O8lJwlOiZPiFs5j5/b+8uEqSKOjyhtOAl7rud2eA5fJTx4liZt36+Cef9lpIjMsmBdbfLvn+hZys5RAFBmGf6nm1zOtfNbu/vC4snalk/f8CJqWmS+tw/fm3p+A8tidRnqRWp8+7d0bmpWHkr8VgHgQZXG/1f2wKysPnd95KX3E68NVGx9QKjdbBNGBo8EwocjJPWYvR78qmtZ0F1kpCfA6nu+7nstqsYKEPMUBDQy2V+ZdSP2RpwHpwlqMibFmFOWhXEHxJNlz7V6YCTEHITjStEqIjtXkpsvqiwPNfVdJ/EnQm8ZEwsUbWEdc7ip5a2w4/VmfFHbDXJgo1PJX20XEWnrQyiHhVgwuK1Lmij6FcXYrUrsCGh8ukgi1dSFVkEJPkag=~-1~-1~-1; "
        "web-session-id=986acfc9-d9cd-4002-904c-33d4d514740a; EVT_FDC_NOTI=N"
    ),
    "priority": "u=0, i",
    "referer": "https://www.coupang.com/np/search?listSize=36&filterType=&rating=0&isPriceRange=true&minPrice=200000&maxPrice=300000&component=&sorter=saleCountDesc&brand=&offerCondition=&filter=1%23attr_12439%2419321%7C497035%23attr_11787%2417899%40DEFAULT&fromComponent=N&channel=user&selectedPlpKeepFilter=&q=%EB%85%B8%ED%8A%B8%EB%B6%81",
    "sec-ch-ua": '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
}

print("connecting...")
res = requests.get(url, headers=headers, timeout=20)
res.raise_for_status()
print(f"<Successfully Connected! | code : {res.status_code}>")

soup = BeautifulSoup(res.text, "lxml")
print(len(res.text))

print("scraping...")

items = soup.find_all("li")
# print(items[0].find("div", attrs={"class":"ProductUnit_productName__gre7e"}).get_text())
print(items)