import numpy as np #수열
import matplotlib.pyplot as plt #시각화
import pandas as pd #파일 다루기
from sklearn import *
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def to_2D(X): # 2차원 배열로 바꾸는 코드
    return(np.array(X).reshape(-1,1))


#데이터 추출
data = pd.read_csv("PythonMLWorkspace(LightWeight)\ScikitLearn\QuizData.csv")
print(data[:4])

X = data.iloc[:,0].values #reception
y = data.iloc[:,-1].values #total

print(X,y)

# train데이터와 test데이터 split
X_train, X_test, y_train, y_test \
= train_test_split(X, y, test_size=0.25, random_state=0)
print(X_train,X_test, y_train, y_test)

# LinearRegression Model 생성
Model_train = LinearRegression()
Model_train.fit(np.array(X_train).reshape(-1,1),np.array(y_train).reshape(-1,1))

Model_test = LinearRegression()
Model_test.fit(np.array(X_test).reshape(-1,1),np.array(y_test).reshape(-1,1))

#시각화
# train
plt.scatter(X_train, y_train, color="blue", s=50)
plt.plot(X_train, Model_train.predict(np.array(X_train).reshape(-1,1)), color="red")
plt.xlabel("Total")
plt.ylabel("Reception")
plt.title("Train Data")
plt.show()

# test
plt.scatter(X_test, y_test, color="blue", s=50)
plt.plot(X_test, Model_test.predict(np.array(X_test).reshape(-1,1)), color="red")
plt.xlabel("Total")
plt.ylabel("Reception")
plt.title("test Data")
plt.show()

# score
print(Model_train.score(to_2D(X_test),to_2D(y_test)))

# predict
total = [[300]] #2차원 배열로 total 선언
print(f"결혼식 참여 인원 300명에 대한 예상 식수 인원은 {Model_train.predict(np.array(total).reshape(-1,1))}명 입니다")