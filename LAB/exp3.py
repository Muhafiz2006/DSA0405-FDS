import numpy as np

house_data = np.loadtxt("House_data.csv", delimiter=",", skiprows=1)

houses_more_than_4 = house_data[house_data[:, 1] > 4]
average_price = np.mean(houses_more_than_4[:, 5])

print("Average price of houses with more than 4 bedrooms: ", round(average_price, 2))
