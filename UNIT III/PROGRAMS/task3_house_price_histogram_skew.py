import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.stats import skew

# NOTE: No house-price dataset was supplied. As a stand-in with the same
# kind of right-skewed monetary distribution, we use the MonthlyIncome
# column from the HR Employee Attrition dataset. Swap in a real house
# price CSV (e.g. Kaggle's House Prices dataset) and change the column
# name below to use actual housing data.
df = pd.read_csv('./employee_attrition.csv')
price_col = df['MonthlyIncome']

price_skew = skew(price_col)
print(f"Skewness of distribution: {price_skew:.3f}")
if price_skew > 0.5:
    verdict = "The data is POSITIVELY (right) SKEWED."
elif price_skew < -0.5:
    verdict = "The data is NEGATIVELY (left) SKEWED."
else:
    verdict = "The data is approximately NORMALLY distributed."
print(verdict)

print("\nDescriptive stats:")
print(price_col.describe())

plt.figure(figsize=(7,5))
plt.hist(price_col, bins=30, color='#4C72B0', edgecolor='black', alpha=0.8)
plt.axvline(price_col.mean(), color='red', linestyle='--', label=f"Mean = {price_col.mean():,.0f}")
plt.axvline(price_col.median(), color='green', linestyle='--', label=f"Median = {price_col.median():,.0f}")
plt.title(f'Histogram of Monthly Income (skew={price_skew:.2f})', fontsize=13, fontweight='bold')
plt.xlabel('Monthly Income ($)')
plt.ylabel('Frequency')
plt.legend()
plt.tight_layout()
plt.savefig('./task3_house_hist.png', dpi=150)
print("\nChart saved.")
