import pandas as pd

# Sales data for the past month, stored in a Pandas DataFrame
data = {
    'CustomerID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    'Age': [25, 34, 25, 41, 34, 28, 25, 34, 41, 30, 28, 25],
    'Product': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'B', 'A', 'C', 'B', 'A'],
    'Amount': [500, 750, 500, 1200, 750, 450, 1200, 750, 500, 900, 450, 500]
}
df = pd.DataFrame(data)

# Frequency distribution of customer ages
age_freq = df['Age'].value_counts().sort_index()

print("Frequency Distribution of Customer Ages:")
print(age_freq)
