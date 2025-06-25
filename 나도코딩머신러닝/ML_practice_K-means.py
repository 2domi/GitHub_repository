print("importing module...")
import numpy as np # 수 배열
import matplotlib.pyplot as plt  #시각화 도구
import pandas as pd # 데이터 분석
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


print("uploading file....")
data = pd.read_csv("PythonMLWorkspace(LightWeight)\
/ScikitLearn/KMeansData.csv")
print(data)

X = data.iloc[:,:].values # (=data.values)
print(X) # X는 데이터 전체

#전체 데이터 분포 시각화
plt.scatter(X[:,0], X[:,1], color="blue")
plt.xlabel("hour")
plt.ylabel("score")
plt.title("Score by Hours")
plt.show()

#축 범위를 동일하게 한 데이터 분포 시각화
plt.scatter(X[:,0], X[:,1], color="blue", s=10)
plt.xlabel("hour")
plt.ylabel("score")
plt.xlim(0,100) # X축의 한계를 100까지로 설정
plt.ylim(0,100) # y의 한계를 100까지로 설정
plt.title("Score by Hours")
plt.show()

#피처 스케일링(Feature Scaling)
scaler = StandardScaler()
X = scaler.fit_transform(X) # X를 표준화
print(X) # 표준화된 X

# Feature Scaling 시각화
plt.figure(figsize=(5,5))
plt.scatter(X[:,0], X[:,1], color="blue")
plt.xlabel("hour")
plt.ylabel("score")
plt.title("Score by Hours")
plt.show()

# Elbow Method
# cluster = 군집, centroid = cluster의 중심, inertia = centroid까지의 거리
inertia_list = []
for i in range(1,11):
    kmeans = KMeans(n_clusters=i, init="k-means++", random_state=0)
    kmeans.fit(X)
    inertia_list.append(kmeans.inertia_) # 각 지점으로부터 클러스터의 중심까지의 거리의 제곱의 합

plt.plot(range(1,11), inertia_list)
plt.xlabel("n_clusters")
plt.ylabel("inertia")
plt.show()

# KMeans 학습
# 모델을 통해 알고싶은것: 어떤 항목이 어떤 cluster에 속해있는지
K = 4 # 최적의 K값

KmeansModel = KMeans(n_clusters=4, random_state = 0)
KmeansModel.fit(X)
y_means = KmeansModel.predict(X)
print(y_means)  # 클러스터 레이블(0~3)만 출력
Centers = KmeansModel.cluster_centers_ #centroid
print(Centers)


# kmeans 학습 결과 시각화
colors = ["r","orange","g","c", "c", "m","brown" ]
plt.figure(figsize=(6,6))
for cluster in range(K):
    plt.scatter(X[y_means == cluster, 0], X[y_means == cluster, 1], s=100, \
                 edgecolors='black', color=colors[cluster]) # 클러스터별 데이터 출력
    plt.scatter(Centers[cluster,0], Centers[cluster,1], color="yellow", \
                edgecolors="black", s=500, marker="s", alpha=0.75) #Centroid 출력
    plt.text(Centers[cluster,0], Centers[cluster,1], cluster, va="center", \
             ha="center", size=20) #클러스터 번호 출력
plt.title("Score by Hours")
plt.xlabel("hour")
plt.ylabel("score")
plt.show()

# Feature Scaling 원상복구 데이터 시각화
X_org = scaler.inverse_transform(X) #데이터를 원상복구
print(X_org)
centers_org = scaler.inverse_transform(Centers) #Centroid 좌표 원상복구

colors = ["r","orange","g","c", "c", "m","brown" ]
plt.figure(figsize=(5,5))
for cluster in range(K):
    plt.scatter(X_org[y_means == cluster, 0], X_org[y_means == cluster, 1], s=100, \
                 edgecolors='black', color=colors[cluster]) # 클러스터별 데이터 출력
    plt.scatter(centers_org[cluster,0], centers_org[cluster,1], color="yellow", \
                edgecolors="black", s=500, marker="s", alpha=0.75) #Centroid 출력
    plt.text(centers_org[cluster,0], centers_org[cluster,1], cluster, va="center", \
             ha="center", size=20) #클러스터 번호 출력
plt.title("Score by Hours")
plt.xlabel("hour")
plt.ylabel("score")
plt.show()