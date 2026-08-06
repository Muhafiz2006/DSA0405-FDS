import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

df = pd.read_csv('./sales_data_sample.csv', encoding='latin1')

Q1 = df['SALES'].quantile(0.25)
Q3 = df['SALES'].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5*IQR
upper = Q3 + 1.5*IQR
cleaned = df[(df['SALES'] >= lower) & (df['SALES'] <= upper)]

print(f"Before removal: n={len(df)}, mean={df['SALES'].mean():.2f}, std={df['SALES'].std():.2f}")
print(f"After removal:  n={len(cleaned)}, mean={cleaned['SALES'].mean():.2f}, std={cleaned['SALES'].std():.2f}")

fig, axes = plt.subplots(2, 2, figsize=(11, 9))

axes[0,0].hist(df['SALES'], bins=30, color='#C44E52', edgecolor='black')
axes[0,0].set_title('Histogram BEFORE Outlier Removal')
axes[0,0].set_xlabel('Sales Amount ($)')
axes[0,0].set_ylabel('Frequency')

axes[0,1].hist(cleaned['SALES'], bins=30, color='#55A868', edgecolor='black')
axes[0,1].set_title('Histogram AFTER Outlier Removal')
axes[0,1].set_xlabel('Sales Amount ($)')
axes[0,1].set_ylabel('Frequency')

axes[1,0].boxplot(df['SALES'], patch_artist=True, boxprops=dict(facecolor='#C44E52'))
axes[1,0].set_title('Box Plot BEFORE Outlier Removal')
axes[1,0].set_ylabel('Sales Amount ($)')

axes[1,1].boxplot(cleaned['SALES'], patch_artist=True, boxprops=dict(facecolor='#55A868'))
axes[1,1].set_title('Box Plot AFTER Outlier Removal')
axes[1,1].set_ylabel('Sales Amount ($)')

plt.tight_layout()
plt.savefig('./task7_before_after.png', dpi=150)
print("\nChart saved.")
