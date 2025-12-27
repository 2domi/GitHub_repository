import requests

res = requests.get("https://naver.com")
res.raise_for_status()
print(f"Successfully Connected | {res}")

with open("naver_html.html", "w", encoding="utf-8") as f:
    f.write(res.text)