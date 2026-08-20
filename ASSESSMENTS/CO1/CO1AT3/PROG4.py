import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([
    [2, 25000, 1200],
    [5, 60000, 1500],
    [3, 40000, 1300],
    [7, 90000, 1800],
    [1, 15000, 1000]
])
y = np.array([650000, 420000, 520000, 300000, 720000])

model = LinearRegression()
model.fit(X, y)

age = float(input("Enter car age (years): "))
kms = float(input("Enter kilometers driven: "))
engine_cc = float(input("Enter engine capacity (cc): "))

new_car = np.array([[age, kms, engine_cc]])
predicted_price = model.predict(new_car)

print(f"Estimated Resale Price: ₹{predicted_price[0]:,.2f}")
