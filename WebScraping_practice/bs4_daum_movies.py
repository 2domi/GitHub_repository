import requests
from bs4 import BeautifulSoup
import re

url = "https://search.daum.net/search?w=tot&q=2020년영화순위"

res = requests.get(url,timeout=10)
res.raise_for_status()
print(f"Successfully Connected | Code : {res.status_code}")

soup = BeautifulSoup(res.text, "lxml")
with open("html_lxml.html","w",encoding="utf8") as f:
    f.write(str(soup))

images = soup.find_all("img")
print(len(images))

# images = soup.find_all(attrs={"width":"232","height":"328"})
# print(images)

# for i in images:
#     print(i["src"])