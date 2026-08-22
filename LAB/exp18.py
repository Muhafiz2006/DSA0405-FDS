"""
Q18. Hospital Age and Body Fat Data Analysis
---------------------------------------------
A hospital tested the age and body fat (%fat) data for 18 randomly
selected adults. This script:
    1. Calculates the mean, median and standard deviation of
       'age' and '%fat' using Pandas.
    2. Draws boxplots for 'age' and '%fat'.
    3. Draws a scatter plot and a Q-Q plot based on these two variables.
"""

import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

# ---------------------------------------------------------------
# 1. Build the data set (as given in the question) into a DataFrame
# ---------------------------------------------------------------
age = [23, 23, 27, 27, 39, 41, 47, 49, 50,
       52, 54, 54, 56, 57, 58, 58, 60, 61]

fat = [9.5, 26.5, 7.8, 17.8, 31.4, 25.9, 27.4, 27.2, 31.2,
       34.6, 42.5, 28.8, 33.4, 30.2, 34.1, 32.9, 41.2, 35.7]

df = pd.DataFrame({"age": age, "%fat": fat})
print("Data set:")
print(df, "\n")

# ---------------------------------------------------------------
# 2. Mean, Median, Standard deviation
# ---------------------------------------------------------------
summary = pd.DataFrame({
    "Mean":   df.mean(),
    "Median": df.median(),
    "Std Dev": df.std()          # sample standard deviation (ddof=1)
})
print("Summary statistics:")
print(summary, "\n")

# ---------------------------------------------------------------
# 3. Boxplots for age and %fat
# ---------------------------------------------------------------
fig, axes = plt.subplots(1, 2, figsize=(10, 5))
df.boxplot(column="age", ax=axes[0])
axes[0].set_title("Boxplot of Age")
axes[0].set_ylabel("Age")

df.boxplot(column="%fat", ax=axes[1])
axes[1].set_title("Boxplot of %Fat")
axes[1].set_ylabel("%Fat")

plt.tight_layout()
plt.savefig("boxplots_age_fat.png", dpi=150)
plt.close()

# ---------------------------------------------------------------
# 4. Scatter plot: age vs %fat
# ---------------------------------------------------------------
plt.figure(figsize=(6, 5))
plt.scatter(df["age"], df["%fat"], color="steelblue", edgecolor="black")
plt.title("Scatter Plot: Age vs %Fat")
plt.xlabel("Age")
plt.ylabel("%Fat")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("scatter_age_fat.png", dpi=150)
plt.close()

# ---------------------------------------------------------------
# 5. Q-Q plots (checking normality) for age and %fat
# ---------------------------------------------------------------
fig, axes = plt.subplots(1, 2, figsize=(10, 5))

stats.probplot(df["age"], dist="norm", plot=axes[0])
axes[0].set_title("Q-Q Plot of Age")

stats.probplot(df["%fat"], dist="norm", plot=axes[1])
axes[1].set_title("Q-Q Plot of %Fat")

plt.tight_layout()
plt.savefig("qqplots_age_fat.png", dpi=150)
plt.close()

print("Saved: boxplots_age_fat.png, scatter_age_fat.png, qqplots_age_fat.png")
