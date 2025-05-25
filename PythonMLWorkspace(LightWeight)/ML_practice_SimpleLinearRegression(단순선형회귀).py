import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDRegressor

data = pd.read_csv("C:/Python_VSCode_Cursor/PythonMLWorkspace(LightWeight)/ScikitLearn/LinearRegressionData.csv")

x = data.iloc[:, :-1].values  #독립변수
y = data.iloc[:, -1].values  #종속변수


reg = LinearRegression()  #선형 회귀 모델 생성
reg.fit(x, y)  #모델 학습
y_pred = reg.predict(x)  #x에 대한 예측
print(y_pred)  #예측 결과 출력

plt.scatter(x,y,color='blue')  #산정도
plt.plot(x, y_pred, color='red')  #선그래프
plt.title('Score by hours')
plt.xlabel('hours')  #x축 레이블
plt.ylabel('score')  #y축 레이블
plt.show()

print()
print()

print(f"9시간 : {reg.predict([[9]])} ")

print(reg.coef_)  #기울기 (m)
print(reg.intercept_)  #y절편 (b)

print()
print()
print()

X_train , X_test , y_train , y_test = train_test_split(x,y,test_size=0.2,random_state=0)   #훈련 데이터와 테스트 데이터 분리(80:20)
print(X_train)
print(X_test)
print(y_train)
print(y_test)

print("================================================")

reg1 = LinearRegression()
reg1.fit(X_train,y_train)

plt.scatter(X_train,y_train,color='blue')  #산정도
plt.plot(X_train, reg1.predict(X_train), color='red')  #선그래프
plt.title('Score by hours(train data)')
plt.xlabel('hours')  #x축 레이블
plt.ylabel('score')  #y축 레이블
plt.show()


reg2 = LinearRegression()
reg2.fit(X_test,y_test)

plt.scatter(X_test,y_test,color='blue')  #산정도
plt.plot(X_test, reg1.predict(X_test), color='red')  #선그래프
plt.title('Score by hours(test data)')
plt.xlabel('hours')  #x축 레이블
plt.ylabel('score')  #y축 레이블
plt.show()

print(f"y = {reg.coef_}X + {reg.intercept_} ")  #전체 데이터 식
print(f"y = {reg1.coef_}X + {reg1.intercept_} ")  #훈련 데이터 식
print(f"y = {reg2.coef_}X + {reg2.intercept_} ")  #테스트 데이터 식

print(f"all set model score: {round(reg.score(x,y)*100,2)}%")
print(f"train set model score: {round(reg.score(X_train,y_train)*100,2)}%")
print(f"test set model score: {round(reg.score(X_test,y_test)*100,2)}%")

model = SGDRegressor(max_iter=1000, eta0=0.001, random_state=0, verbose=1)
model.fit(X_train,y_train)

plt.scatter(X_train,y_train,color='blue')  #산정도
plt.plot(X_train,model.predict(X_train),color='red')  #선그래프
plt.title('Score by hours(train data,SGD)')
plt.xlabel('hours')  #x축 레이블
plt.ylabel('score')  #y축 레이블
plt.show()

print(f"SGD 모델(test) 점수 : {round(model.score(X_test,y_test)*100,2)}%")
print(f"SGD 모델(train) 점수 : {round(model.score(X_train,y_train)*100,2)}%")
print(f"SGD 모델 점수 : {round(model.score(x,y)*100,2)}%")