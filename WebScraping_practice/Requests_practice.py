import requests as res

url = "https://www.google.com/"
site = res.get(url)

site.raise_for_status() # 접속 가능이면 그대로 진행, 접속 불가이면 에러
print("Successfully Connected | Code :",site.status_code)

print(site.text)

with open("google_html.html", "w", encoding="utf8")as f: # 구글의 html을 파일로 반환
    f.write(site.text)

