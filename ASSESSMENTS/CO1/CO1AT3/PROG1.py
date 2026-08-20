import numpy as np

house_data = np.array([
    [3, 1400, 7500000],
    [5, 2200, 12500000],
    [4, 1800, 9800000],
    [6, 3000, 18500000],
    [2, 1100, 5200000]
])

bedrooms = house_data[:, 0]
sale_price = house_data[:, 2]

mask = bedrooms > 4
avg_price = np.mean(sale_price[mask])

print("Houses with >4 bedrooms:\n", house_data[mask])
print("Average Sale Price:", avg_price)
