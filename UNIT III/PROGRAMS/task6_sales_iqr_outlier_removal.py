import pandas as pd

df = pd.read_csv('./sales_data_sample.csv', encoding='latin1')
print(f"Original dataset shape: {df.shape}")

Q1 = df['SALES'].quantile(0.25)
Q3 = df['SALES'].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5*IQR
upper = Q3 + 1.5*IQR
print(f"Q1={Q1:.2f}, Q3={Q3:.2f}, IQR={IQR:.2f}, Lower={lower:.2f}, Upper={upper:.2f}")

cleaned = df[(df['SALES'] >= lower) & (df['SALES'] <= upper)].reset_index(drop=True)
print(f"\nRows removed: {len(df) - len(cleaned)}")
print(f"Cleaned dataset shape: {cleaned.shape}")

print("\nFirst 10 rows of cleaned dataset (key columns):")
print(cleaned[['ORDERNUMBER','QUANTITYORDERED','PRICEEACH','SALES','PRODUCTLINE','COUNTRY']].head(10).to_string(index=False))

cleaned.to_csv('./sales_data_cleaned.csv', index=False)
print("\nCleaned dataset saved to sales_data_cleaned.csv")
