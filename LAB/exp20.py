"""
Q20. Customer Segmentation
-----------------------------
a) Load "customer_data.csv" into a Pandas DataFrame. Expected columns:
   'Customer ID', 'Age', 'Gender', 'Total Spending'.
b) Segment customers into three groups based on Total Spending:
   "High Spenders", "Medium Spenders", "Low Spenders". Assign these
   segments to a new column in the DataFrame.
c) Calculate the average age of customers in each spending segment.

NOTE: Place "customer_data.csv" in the same folder as this script
before running it. If the file is not found, a small sample file is
generated automatically so the script can still be demonstrated.
"""

import os
import numpy as np
import pandas as pd

CSV_FILE = "customer_data.csv"

# ---------------------------------------------------------------
# Create a sample customer_data.csv if it does not already exist
# (so the script can be run/tested end-to-end).
# Remove this block once you have your real data file.
# ---------------------------------------------------------------
if not os.path.exists(CSV_FILE):
    rng = np.random.default_rng(42)
    n = 20
    sample = pd.DataFrame({
        "Customer ID": range(1, n + 1),
        "Age": rng.integers(18, 65, size=n),
        "Gender": rng.choice(["Male", "Female"], size=n),
        "Total Spending": rng.integers(50, 5000, size=n)
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
# b) Segment customers into three groups based on Total Spending
#    using tertiles (equal-sized groups). pd.qcut splits the data
#    into three bins with (roughly) equal numbers of customers.
# ---------------------------------------------------------------
df["Spending Segment"] = pd.qcut(
    df["Total Spending"],
    q=3,
    labels=["Low Spenders", "Medium Spenders", "High Spenders"]
)

print("Data with 'Spending Segment' column:")
print(df, "\n")

# ---------------------------------------------------------------
# c) Average age of customers in each spending segment
# ---------------------------------------------------------------
avg_age_by_segment = (
    df.groupby("Spending Segment", observed=True)["Age"]
      .mean()
      .reset_index()
      .rename(columns={"Age": "Average Age"})
)

print("Average age of customers by spending segment:")
print(avg_age_by_segment.to_string(index=False))
