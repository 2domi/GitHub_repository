print("모듈 불러오는중...")
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures, MinMaxScaler
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def date_to_year_fraction(date):
    year = date.year
    month = date.month
    day = date.day
    return year + (month - 1) / 12 + (day - 1) / 365


print("데이터 불러오는중...")
dataset = pd.read_csv(r"C:\Python_VSCode_Cursor\XAU_1d_data.csv", sep=";")

dataset["Date"] = pd.to_datetime(dataset["Date"])
X = (dataset["Date"].apply(date_to_year_fraction).values.reshape(-1, 1))
y = dataset["Open"].values


scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

print(X)
print(y)

# # 데이터 시각화
# plt.scatter(X, y, s=1)
# plt.xlabel("Date")
# plt.ylabel("Gold Price")
# plt.title("Gold Price")
# plt.show()

print("Poly 객체로 변환...")
Poly_regression = PolynomialFeatures(degree=7)
Poly_X = Poly_regression.fit_transform(X_scaled)
X_more = np.linspace(0, 2, 1000).reshape(-1, 1)
Poly_X_more = Poly_regression.transform(X_more)

Poly_model = LinearRegression()
Poly_model.fit(Poly_X,y)



# 데이터 시각화
plt.scatter(X_scaled, y, s=1)
plt.plot(X_scaled, Poly_model.predict(Poly_X), color="r")
plt.xlabel("Date (scaled)")
plt.ylabel("Gold Price")
plt.title("Gold Price per Day")
# plt.xlim(0, 2)
# plt.ylim(380, 10000)
plt.show()

# year = float(input("예측할 년도: "))
# year = [[year]]
# Poly_year = Poly_regression.transform(year)

# print(Poly_model.predict(Poly_year))