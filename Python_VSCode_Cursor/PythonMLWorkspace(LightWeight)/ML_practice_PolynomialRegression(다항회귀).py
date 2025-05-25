import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

data = pd.read_csv("C:\Python_VSCode_Cursor\PythonMLWorkspace(LightWeight)\ScikitLearn\PolynomialRegressionData.csv")
X = data.iloc[:, :-1].values #처음부터 마지막 전까지의 변수(독립변수)
y = data.iloc[:, -1].values #마지막 변수(종속변수)

# <Simple Linear Regression>
LinearRegression_model = LinearRegression()
LinearRegression_model.fit(X,y) # 학습


# <Polynomial Regression>
PolynomialRegression4 = PolynomialFeatures(degree=4) # degree : 차수
PolynomialRegression3 = PolynomialFeatures(degree=3) # degree : 차수
PolynomialRegression2 = PolynomialFeatures(degree=2) # degree : 차수

X_poly2 = PolynomialRegression2.fit_transform(X) # [X] -> [1, x^1, x^2] ex) X = 3 -> [1,3,9]
X_poly3 = PolynomialRegression3.fit_transform(X) # [X] -> [1, x^1, x^2] ex) X = 3 -> [1,3,9]
X_poly4 = PolynomialRegression4.fit_transform(X) # [X] -> [1, x^1, x^2] ex) X = 3 -> [1,3,9]

poly_model2 = LinearRegression()
poly_model3 = LinearRegression()
poly_model4 = LinearRegression()
poly_model2.fit(X_poly2, y) #변환된 X,y를 가지고 모델 생성
poly_model3.fit(X_poly3, y) #변환된 X,y를 가지고 모델 생성
poly_model4.fit(X_poly4, y) #변환된 X,y를 가지고 모델 생성


#데이터 시각화
X_range = np.linspace(min(X), max(X), 100).reshape(-1,1) # X를 0.1단위로 잘라 데이터 생성

plt.scatter(X,y, color="blue")
plt.plot(X_range,poly_model2.predict(PolynomialRegression2.fit_transform(X_range)), color="orange")
plt.plot(X_range,poly_model3.predict(PolynomialRegression3.fit_transform(X_range)), color="green")
plt.plot(X_range,poly_model4.predict(PolynomialRegression4.fit_transform(X_range)), color="purple")
plt.plot(X,LinearRegression_model.predict(X), color = "red")
plt.title("Score by hours (GENIUS)")
plt.xlabel("hours")
plt.ylabel("score")
plt.show()

#<시험 성적 예측>
print(LinearRegression_model.predict([[2]])) # X = 2  -> y = ? (단순선형회귀)
print(poly_model3.predict(PolynomialRegression3.fit_transform([[2]]))) #2를 3차 다항식으로 변환 후 예측

#점수
print(LinearRegression_model.score(X,y))
print(poly_model3.score(X_poly3, y))