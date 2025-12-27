print("모듈 불러오는중...")

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix



print("데이터 불러오는중...")

data = pd.read_csv("PythonMLWorkspace(LightWeight)\ScikitLearn\LogisticRegressionData.csv")
X = data.iloc[:, :-1].values  # 마지막 열을 제외한 모든 열
y = data.iloc[:, -1].values   # 마지막 열만

#데이터 분리
print("데이터 분리하는중...")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

#모델 학습
print("모델 학습중...")

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train, y_train)

#예측
print("예측중...")

pred = float(input("예측할 시간: "))
print("예측:", model.predict([[pred]]))  # 예측된 클래스 (0 또는 1)
print("확률:",model.predict_proba([[pred]])[0][1]*100)  # 클래스 1에 대한 확률만

#평가
print("평가중...")

print("모델 성능:", model.score(X_test, y_test)*100)
print("실제", y_test)
print("예측", model.predict(X_test))
print("공부시간\n", X_test)

#데이터 시각화
print("데이터 시각화중...")

X_range = np.arange(X_train.min(), X_train.max() , 0.1).reshape(-1,1) # X값을 0.1마다 촘촘히 배치
print("데이터 시각화용 X값 확장\n", X_range)

plt.scatter(X_train,y_train, color = "red")
plt.plot(X_range, model.predict_proba(X_range)[:,1], color = "blue") #로지스틱 회귀 모델
plt.axhline(y=0.5, color="green", linestyle=":") #중앙선
plt.title("Pass/Fail Based on Study Hours")
plt.xlabel("hours")
plt.ylabel("predict")
plt.show()
print("==================")

#혼동 행렬 (Confusion Matrix)
cm = confusion_matrix(y_test, model.predict(X_test))
print(cm)

"""       예측 0 예측 1
실제 0    [ TN  ,  FP ] 
실제 1    [ FN  ,  TP ]
"""

cm_all = confusion_matrix(y, model.predict(X))
print(cm_all)