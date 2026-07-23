import pandas as pd

df = pd.read_csv("grocerystore.csv")
total_sales = df["Sales"].sum()
print("Total sales for the grocery store: ", round(total_sales, 2))

discount = 0.10
tax = 0.18
price_after_discount = total_sales - (total_sales * discount)
price_after_tax = price_after_discount + (price_after_discount * tax)

print("Final amount after applying discount and tax: ", round(price_after_tax, 2))
