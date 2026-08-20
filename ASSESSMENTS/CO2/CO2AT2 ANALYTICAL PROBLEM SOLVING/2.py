import pandas as pd
df = pd.DataFrame({
 "Name": ["John", "Emma", "Liam", "Olivia"],
 "Age": [20, 19, 21, 18],
 "Student": [True, True, False, True]
})
print(df)
new_row = pd.DataFrame(
 [["Sophia", 22, False]],
 columns=["Name", "Age", "Student"]
)
df = pd.concat([df, new_row], ignore_index=True)
print(df)
