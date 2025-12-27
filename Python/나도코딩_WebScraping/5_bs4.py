import requests
from bs4 import BeautifulSoup
import warnings

warnings.filterwarnings("ignore")

url = "https://sports.daum.net/baseball"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"}

res = requests.get(url, headers=headers)
res.raise_for_status()
res.encoding = "utf-8"

# with open("response.html", "w", encoding="utf-8") as f:
#     f.write(res.text)

soup = BeautifulSoup(res.text, "lxml")
ranks = soup.findAll("a", attrs={"data-tiara-layer":"rankingnews popular news_list"})
for rank in ranks[1:]:
    print(rank.get_text())

print("===========================================")

all_news = soup.find_all("strong", attrs={"class":"tit_thumb"})
for news in all_news:
    print(news.get_text())