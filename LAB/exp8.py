import pandas as pd

df = pd.read_csv("Sales_data.csv")
top_5_products = df.groupby("Product_Name")["Price"].sum().nlargest(5)

print("Five most sold products: ", top_5_products)
