import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
data = {
 "Name": [" Alice ", "Bob", "Charlie", "Diana", "Evan"],
 "Department": ["HR", "Engineering", "HR", "Engineering", "Marketing"],
 "Salary": [50000, 85000, np.nan, 92000, 60000],
 "Join_Date": ["2022-01-15", "2021-06-20", "2023-03-11",
 "2020-11-01", "2024-02-28"]
}
df = pd.DataFrame(data)
# Preprocessing
df["Name"] = df["Name"].str.strip()
df["Salary"] = df["Salary"].fillna(df["Salary"].median())
df["Join_Date"] = pd.to_datetime(df["Join_Date"])
df["Years_of_Service"] = 2026 - df["Join_Date"].dt.year
# Aggregation
summary = df.groupby("Department").agg(
 Avg_Salary=("Salary", "mean"),
 Total_Employees=("Name", "count")
).reset_index()
print(summary)
# Visualization
sns.barplot(data=summary, x="Department", y="Avg_Salary")
plt.title("Average Salary by Department")
plt.show()
sns.scatterplot(data=df, x="Years_of_Service", y="Salary",
 hue="Department")
plt.title("Salary vs Years of Service")
plt.show()
