import numpy as np

sales_data = np.genfromtxt("Sales_data.csv", delimiter=",", skip_header=1, dtype=str)

months = sales_data[:, 1]
sales = sales_data[:, 4].astype(float)

Q1 = 0.0
Q4 = 0.0

for i in range(len(months)):
    if ("January" in months[i]) or ("February" in months[i]) or ("March" in months[i]):
        Q1 += sales[i]
    elif ("October" in months[i]) or ("November" in months[i]) or ("December" in months[i]):
        Q4 += sales[i]

total_sales_year = np.sum(sales)

percentage_increase = ((Q4 - Q1) / Q1) * 100

print("Total sales for the year:", round(total_sales_year, 2))
print("Percentage increase from Q1 to Q4:", round(percentage_increase, 2), "%")
