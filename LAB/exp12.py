import matplotlib.pyplot as plt

# Monthly average temperature data for a city (in Celsius)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
temperature = [18, 20, 24, 28, 32, 34, 31, 30, 29, 26, 22, 19]

# Monthly rainfall data for the same city (in mm)
rainfall = [10, 15, 20, 40, 90, 180, 220, 200, 150, 80, 30, 12]

# 1. Line plot - monthly temperature data
plt.figure(figsize=(8, 5))
plt.plot(months, temperature, marker='o', color='tomato', linewidth=2)
plt.title("Monthly Temperature Data (Line Plot)")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.tight_layout()
plt.show()

# 2. Scatter plot - monthly rainfall data
plt.figure(figsize=(8, 5))
plt.scatter(months, rainfall, color='teal', s=80)
plt.title("Monthly Rainfall Data (Scatter Plot)")
plt.xlabel("Month")
plt.ylabel("Rainfall (mm)")
plt.tight_layout()
plt.show()
