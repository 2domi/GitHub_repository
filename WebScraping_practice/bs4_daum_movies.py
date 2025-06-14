import requests
from bs4 import BeautifulSoup
import re

url = "https://search.daum.net/search?w=tot&q=2020년영화순위"

res = requests.get(url,timeout=10)
res.raise_for_status()
print(f"Successfully Connected | Code : {res.status_code}")

soup = BeautifulSoup(res.text, "lxml")

images = soup.find_all("img", attrs={"data-original-loaded":"true"})
print(images)

for i in images:
    print(i["src"])