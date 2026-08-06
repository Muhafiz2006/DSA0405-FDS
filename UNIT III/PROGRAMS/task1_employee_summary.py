import pandas as pd
pd.set_option('display.width', 120)
pd.set_option('display.max_columns', 20)

df = pd.read_csv('./employee_attrition.csv')

print("="*70)
print("EMPLOYEE DATASET SUMMARY (IBM HR Analytics Employee Attrition Dataset)")
print("="*70)

print(f"\n1. Number of rows: {df.shape[0]}")
print(f"2. Number of columns: {df.shape[1]}")

print("\n3. Data types:")
print(df.dtypes)

print("\n4. Missing values (per column):")
missing = df.isnull().sum()
print(missing[missing > 0] if missing.sum() > 0 else "No missing values found in this dataset.")

# Focus the statistical summary on the core numeric HR metrics for readability
key_numeric = ['Age', 'DailyRate', 'DistanceFromHome', 'MonthlyIncome',
                'PercentSalaryHike', 'TotalWorkingYears', 'YearsAtCompany']
print("\n5. Statistical summary (key numeric columns):")
print(df[key_numeric].describe())

key_cat = ['Attrition', 'Department', 'JobRole', 'Gender', 'MaritalStatus']
print("\n6. Statistical summary (key categorical columns):")
print(df[key_cat].describe())
