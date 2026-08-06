import pandas as pd

df = pd.read_csv('./students_performance.csv')

Q1 = df['math score'].quantile(0.25)
Q3 = df['math score'].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5*IQR
upper = Q3 + 1.5*IQR

print(f"Q1 = {Q1:.2f}")
print(f"Q3 = {Q3:.2f}")
print(f"IQR = {IQR:.2f}")
print(f"Lower bound = {lower:.2f}")
print(f"Upper bound = {upper:.2f}")

outliers = df[(df['math score'] < lower) | (df['math score'] > upper)]
print(f"\nNumber of outliers detected: {len(outliers)}")
print("\nOutlier records:")
print(outliers[['gender', 'math score', 'reading score', 'writing score']].to_string(index=False))
