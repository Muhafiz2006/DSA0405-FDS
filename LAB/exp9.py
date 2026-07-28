import pandas as pd

df = pd.read_csv("house.csv")

location_price_average = df.groupby("Location")["price"].mean()
more_than_4beds = df[df["beds"] > 4].count()["beds"]
largest_sq_feet = df["size"].max()

print("Average house price for each location: ", location_price_average)
print("Number of houses with more than 4 bedrooms: ", more_than_4beds)
print("Largest house size: ", largest_sq_feet)
