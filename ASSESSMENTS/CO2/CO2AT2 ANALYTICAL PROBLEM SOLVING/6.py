from scipy.stats import pearsonr
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
correlation, p_value = pearsonr(x, y)
print("Correlation:", correlation)
