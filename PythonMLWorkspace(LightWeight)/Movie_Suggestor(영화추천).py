### 인구 통계학적 필터링 ###

print("<Importing Modules>")
import pandas as pd
import numpy as np

# 파일 불러오기
print("<Uploading Files>")

df1 = pd.read_csv(r"C:\Python_VSCode_Cursor\tmdb_5000_credits.csv")
df2 = pd.read_csv(r"C:\Python_VSCode_Cursor\tmdb_5000_movies.csv")

print(df1.head())
print(df2.head())

# 파일 합치기
print("<Merging Files>")

df1.columns = ["id","title","cast","crew"] # column 이름 바꾸기
print(df1[["id","cast","crew"]]) # title은 중복이니 없앤 값 출력
df = df2.merge(df1[["id","cast","crew"]], on="id") # id를 기준으로 df1과 df2의 데이터 합치기

print(df)

"""
#df는 df1과 df2를 합친 값
# <모두가 좋아하는 영화>
print("<Movie: All people Like>")
C = df["vote_average"].mean() # .mean() : 평균
print(f"C(투표수 평균): {C}")

m = df2["vote_count"].quantile(0.9) # .quantile() : 데이터의 하위 X%
print(f"m(상위 10%의 투표수): {m}")

q_movies = df2.copy().loc[df2["vote_count"] >= m] # .copy()를 사용해 원본 데이터를 수정하지 않고
                                                  # .loc[]을 사용해 행과 열을 선택
                                                  # vote_count라는 column의 값이 m보다 큰 것만 골라 q_movies에 저장
                                                  # -> q_movies : vote_count가 상위 10%인 row만 뺴서 만든 리스트
print(q_movies)
print(q_movies["vote_count"].sort_values())

def weighted_rating(x, m=m, C=C): # 값을 지정하지 않으면 원래 있던 값으로 지정
    v = x["vote_count"]
    R = x["vote_average"]
    return ((v/(v+m)*R)+(m/(m+v)*C))

q_movies["score"] = q_movies.apply(weighted_rating, axis=1) #score라는 이름으로 row단위로 weighted_rating 함수를 호출한 값
q_movies = q_movies.sort_values(by="score", ascending=False) #내림차순으로 정렬
print(q_movies[["title", "vote_count", "vote_average", "score"]])

#시각화
pop= df2.sort_values('popularity', ascending=False)
import matplotlib.pyplot as plt
plt.figure(figsize=(12,4))

plt.barh(pop['title'].head(10),pop['popularity'].head(10), align='center',
        color='skyblue')
plt.gca().invert_yaxis()
plt.xlabel("Popularity")
plt.title("Popular Movies")
plt.show()
"""

### 컨텐츠 기반 필터링 ###

print(df["overview"])
