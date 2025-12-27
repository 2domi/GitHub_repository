import requests

url = "https://wikipedia.org"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"}

res = requests.get(url, headers=headers) # 원래는 접근 권한 x (403)

res.raise_for_status() # 연결 확인

print("===== Start WebScraping =====")

with open("Wikipedia.html", "w", encoding="utf-8") as f :
    f.write(res.text)