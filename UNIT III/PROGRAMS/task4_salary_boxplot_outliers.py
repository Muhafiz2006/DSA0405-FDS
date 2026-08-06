import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

df = pd.read_csv('./ds_salaries.csv')

Q1 = df['salary_in_usd'].quantile(0.25)
Q3 = df['salary_in_usd'].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5*IQR
upper = Q3 + 1.5*IQR
outliers = df[(df['salary_in_usd'] < lower) | (df['salary_in_usd'] > upper)]

print(f"Q1 = {Q1:.2f}, Q3 = {Q3:.2f}, IQR = {IQR:.2f}")
print(f"Lower bound = {lower:.2f}, Upper bound = {upper:.2f}")
print(f"\nNumber of outliers detected: {len(outliers)}")
print("\nOutlier records (job title, salary in USD):")
print(outliers[['job_title', 'experience_level', 'salary_in_usd']].to_string(index=False))

plt.figure(figsize=(6,6))
bp = plt.boxplot(df['salary_in_usd'], vert=True, patch_artist=True,
                  boxprops=dict(facecolor='#87CEEB'),
                  medianprops=dict(color='red', linewidth=2),
                  flierprops=dict(markerfacecolor='red', marker='o', markersize=6))
plt.title('Box Plot of Data Science Salaries (USD)', fontsize=13, fontweight='bold')
plt.ylabel('Salary (USD)')
plt.tight_layout()
plt.savefig('./task4_salary_box.png', dpi=150)
print("\nChart saved.")
