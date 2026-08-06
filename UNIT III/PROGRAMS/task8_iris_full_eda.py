import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

df = pd.read_csv('./iris.csv')
df = df.drop(columns=['Id'])

print("="*70)
print("1. DATASET INFORMATION")
print("="*70)
print(f"Shape: {df.shape}")
print(df.dtypes)

print("\n" + "="*70)
print("2. MISSING VALUES")
print("="*70)
missing = df.isnull().sum()
print(missing)
if missing.sum() == 0:
    print("(No missing values found in this dataset.)")

print("\n" + "="*70)
print("3. DESCRIPTIVE STATISTICS")
print("="*70)
print(df.describe())

num_cols = [c for c in df.columns if c != 'Species']

# 4. Histograms
fig, axes = plt.subplots(2, 2, figsize=(11, 9))
for ax, col in zip(axes.flat, num_cols):
    ax.hist(df[col], bins=20, color='#4C72B0', edgecolor='black')
    ax.set_title(f'Histogram: {col}')
    ax.set_xlabel(col)
    ax.set_ylabel('Frequency')
plt.tight_layout()
plt.savefig('./task8_histograms.png', dpi=150)

# 5. Box plots
fig2, ax2 = plt.subplots(figsize=(8, 6))
ax2.boxplot([df[c] for c in num_cols], tick_labels=num_cols, patch_artist=True,
            boxprops=dict(facecolor='#87CEEB'))
ax2.set_title('Box Plots of Iris Features')
ax2.set_ylabel('cm')
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig('./task8_boxplots.png', dpi=150)

# 6. Outlier detection (IQR) per numeric column
print("\n" + "="*70)
print("4. OUTLIER DETECTION (IQR METHOD)")
print("="*70)
outlier_mask = pd.Series(False, index=df.index)
for col in num_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5*IQR
    upper = Q3 + 1.5*IQR
    col_outliers = (df[col] < lower) | (df[col] > upper)
    print(f"{col}: {col_outliers.sum()} outliers (bounds: {lower:.2f} - {upper:.2f})")
    outlier_mask = outlier_mask | col_outliers

print(f"\nTotal rows flagged as outliers (any feature): {outlier_mask.sum()}")

# 7. Remove outliers
df_cleaned = df[~outlier_mask].reset_index(drop=True)
print("\n" + "="*70)
print("5. CLEANED DATASET")
print("="*70)
print(f"Shape before cleaning: {df.shape}")
print(f"Shape after cleaning:  {df_cleaned.shape}")

# 8. Save cleaned dataset
df_cleaned.to_csv('./iris_cleaned.csv', index=False)
print("\nCleaned dataset saved to iris_cleaned.csv")
