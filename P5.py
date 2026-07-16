import numpy as np
from sklearn.tree import DecisionTreeClassifier, export_text

X = np.array([
    [45000, 720, 0],
    [30000, 650, 1],
    [60000, 780, 0],
    [28000, 620, 2],
    [52000, 710, 1]
])
y = np.array([1, 0, 1, 0, 1])

model = DecisionTreeClassifier(criterion='gini', random_state=42)
model.fit(X, y)

new_applicant = np.array([[48000, 700, 1]])
prediction = model.predict(new_applicant)
print("Prediction (1=Approved, 0=Rejected):", prediction[0])

feature_names = ["Income", "Credit_Score", "Existing_Loans"]
rules = export_text(model, feature_names=feature_names)
print("\nDecision Rules:\n", rules)
