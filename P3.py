import numpy as np
from sklearn.linear_model import LogisticRegression

X = np.array([
    [1, 3, 120],
    [6, 15, 300],
    [0, 1, 80],
    [4, 10, 250],
    [2, 5, 160]
])
y = np.array([0, 1, 0, 1, 0])

model = LogisticRegression()
model.fit(X, y)

new_email = np.array([[3, 8, 200]])  # different sample so it's not identical to Q2
prediction = model.predict(new_email)
probability = model.predict_proba(new_email)

print("Prediction (1=Spam, 0=Not Spam):", prediction[0])
print("Probability [Not Spam, Spam]:", probability[0])
