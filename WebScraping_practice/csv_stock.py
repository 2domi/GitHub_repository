import csv
import requests 
from bs4 import BeautifulSoup

url = "http://data.krx.co.kr/contents/MMC/RANK/rank/MMCRANK001.cmd"

# Header 지정
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate",
    "accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "max-age=0",
    "connection": "keep-alive",
    "cookie": "__smVisitorID=VV8n4tnyu-I; JSESSIONID=sGYWR7i1hrKPokmjfwSCfq4fh0JLMscdHbCKa0NyjEYBehQWlLEo5kIvCv0EL7Zq.bWRjX2RvbWFpbi9tZGNvd2FwMi1tZGNhcHAwMQ==",
    "host": "data.krx.co.kr",
    "referer": "https://www.google.com/",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
}



res = requests.get(url,headers=headers)
res.raise_for_status()
print(f"<Successfully Connected! | Code:{res.status_code}>")

Soup = BeautifulSoup(res.text, "html.parser")
# print(Soup.prettify())

print(Soup.find_all(attrs={"class":["tui-grid-row-even","tui-grid-row-odd"]}))