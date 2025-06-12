import requests as res

# UserAgent 설정
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"}

url = "https://nadocoding.tistory.com"
site = res.get(url, headers=headers)

site.raise_for_status() # 접속 가능이면 그대로 진행, 접속 불가이면 에러
print("Successfully Connected | Code :",site.status_code)

print(site.text)

with open("nadocoding_tistory.html", "w", encoding="utf8")as f: # 구글의 html을 파일로 반환
    f.write(site.text)