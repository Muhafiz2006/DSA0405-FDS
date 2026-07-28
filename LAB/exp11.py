import matplotlib.pyplot as plt

# Monthly sales data for a product (units sold)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales = [220, 245, 260, 210, 275, 300, 320, 290, 310, 330, 350, 400]

# 1. Line plot - monthly sales trend
plt.figure(figsize=(8, 5))
plt.plot(months, sales, marker='o', color='steelblue', linewidth=2)
plt.title("Monthly Sales Trend (Line Plot)")
plt.xlabel("Month")
plt.ylabel("Units Sold")
plt.tight_layout()
plt.show()

# 2. Scatter plot - monthly sales
plt.figure(figsize=(8, 5))
plt.scatter(months, sales, color='crimson', s=80)
plt.title("Monthly Sales (Scatter Plot)")
plt.xlabel("Month")
plt.ylabel("Units Sold")
plt.tight_layout()
plt.show()

# 3. Bar plot - monthly sales data
plt.figure(figsize=(8, 5))
plt.bar(months, sales, color='darkorange')
plt.title("Monthly Sales Data (Bar Plot)")
plt.xlabel("Month")
plt.ylabel("Units Sold")
plt.tight_layout()
plt.show()
