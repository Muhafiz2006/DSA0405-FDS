from scipy import stats
data = [22, 25, 19, 24, 28, 30]
t_stat, p_value = stats.ttest_1samp(data, 25)
print("T-Statistic:", t_stat)
print("P-Value:", p_value)
