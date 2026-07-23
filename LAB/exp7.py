import pandas as pd

df = pd.read_csv("order_data.csv")
total_orders = df.groupby("Full Name")["Order Count"].sum()
avg_order_per_product = df.groupby("Items")["Order Total"].mean()
earliest_order = df["Order"].min()
latest_order = df["Order"].max()

print("Total number of orders made by each customer: ", total_orders)
print("Average order quantity for each product: ", avg_order_per_product)
print("Earliest order date: ", earliest_order)
print("Latest order date: ", latest_order)
