import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

#<데이터 가져오고 변수 분리>
data = pd.read_csv("C:\Python_VSCode_Cursor\PythonMLWorkspace(LightWeight)\ScikitLearn\MultipleLinearRegressionData.csv") # 데이터 불러오기
X = data.iloc[:,:-1] # 독립변수
y = data.iloc[:,-1] # 종속변수

#<one-hot encoding>
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(drop="first"), [2])], remainder = 'passthrough')
X = ct.fit_transform(X)
print(X)    

#<데이터 분리>
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

#<다중선형회귀모델 학습>
Model = LinearRegression()
Model.fit(X_train, y_train)

#<예측 값과 실제 값 비교&모델 점수>
y_pred = Model.predict(X_test)
print(y_pred)
print(y_test)
print(round(Model.score(X_test, y_test)*100, 2),"%")
print(Model.coef_)
print(Model.intercept_)

#<모델 평가>
#MAE : 실제값과 예측값 차이의 절대값 (0에 가까울수록 좋음)
#MSE : 실제값과 예측값 차이의 제곱 (0에 가까울수록 좋음)
#RMSE : 실제값과 예측값 차이의 제곱의 루트(MSE의 루트) (0에 가까울수록 좋음)
#R2 : 결정 계수 (1에 가까울수록 좋음)(=Model.score(X_test, y_test))

print("MAE : ",mean_absolute_error(y_test, y_pred)) #실제값, 예측값
print("MSE : ",mean_squared_error(y_test, y_pred))
print("RMSE : ",np.sqrt(mean_squared_error(y_test, y_pred)))
print("R2 : ",r2_score(y_test, y_pred))