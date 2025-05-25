import matplotlib.pyplot as plt


### 제곱 그래프 ###
X = []
for i in range(1000):
    X.append(i - 500) # -500 ~ 499

Y = []
for i in X:
    Y.append(i**2) # X의 제곱

plt.plot(X, Y, color="red") #그래프 생성

plt.axvline(x=0, color='blue', linestyle='--') # y좌표 0에 수평선

plt.show()