"""
Q19. Sales and Profit Analysis
--------------------------------
a) Load "sales_data.csv" into a Pandas DataFrame. Expected columns:
   'Date', 'Product', 'Quantity Sold', 'Unit Price'.
b) Create a new column 'Total Sales' = Quantity Sold * Unit Price.
c) Calculate the total sales for each product and the overall profit
   (assuming a 20% profit margin on each product). Display the top 5
   most profitable products.

NOTE: Place "sales_data.csv" in the same folder as this script before
running it. If the file is not found, a small sample file is
generated automatically so the script can still be demonstrated.
"""

import os
import pandas as pd

CSV_FILE = "sales_data.csv"
PROFIT_MARGIN = 0.20   # 20% profit margin

# ---------------------------------------------------------------
# Create a sample sales_data.csv if it does not already exist
# (so the script can be run/tested end-to-end).
# Remove this block once you have your real data file.
# ---------------------------------------------------------------
if not os.path.exists(CSV_FILE):
    sample = pd.DataFrame({
        "Date": ["2024-01-01", "2024-01-02", "2024-01-03", "2024-01-04",
                 "2024-01-05", "2024-01-06", "2024-01-07", "2024-01-08",
                 "2024-01-09", "2024-01-10"],
        "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Laptop",
                    "Webcam", "Mouse", "Monitor", "Keyboard", "Webcam"],
        "Quantity Sold": [3, 10, 7, 4, 2, 6, 8, 5, 9, 12],
        "Unit Price": [750.00, 15.00, 25.00, 180.00, 750.00,
                        40.00, 15.00, 180.00, 25.00, 40.00]
    })
    sample.to_csv(CSV_FILE, index=False)
    print(f"'{CSV_FILE}' not found — a sample file was generated for demo purposes.\n")

# ---------------------------------------------------------------
# a) Load the CSV file into a DataFrame
# ---------------------------------------------------------------
df = pd.read_csv(CSV_FILE)
print("Loaded data:")
print(df, "\n")

# ---------------------------------------------------------------
# b) Create 'Total Sales' column
# ---------------------------------------------------------------
df["Total Sales"] = df["Quantity Sold"] * df["Unit Price"]
print("Data with 'Total Sales' column:")
print(df, "\n")

# ---------------------------------------------------------------
# c) Total sales per product & overall profit (20% margin)
# ---------------------------------------------------------------
product_sales = (
    df.groupby("Product")["Total Sales"]
      .sum()
      .reset_index()
      .rename(columns={"Total Sales": "Total Sales Amount"})
)

# Profit per product = 20% of that product's total sales
product_sales["Profit"] = product_sales["Total Sales Amount"] * PROFIT_MARGIN

# Overall profit across all products
overall_profit = product_sales["Profit"].sum()

print("Total sales & profit by product:")
print(product_sales, "\n")

print(f"Overall profit (20% margin on all sales): {overall_profit:.2f}\n")

# ---------------------------------------------------------------
# Top 5 most profitable products
# ---------------------------------------------------------------
top5 = product_sales.sort_values("Profit", ascending=False).head(5)
print("Top 5 most profitable products:")
print(top5.to_string(index=False))
