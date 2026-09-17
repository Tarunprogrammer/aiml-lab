import pandas as pd

# Load the dataset
# Note: Ensure the filename matches (students.csv)
df = pd.read_csv('students.csv')

print("--- Full DataFrame ---")
print(df)

print("\n--- Accessing Specific Rows (Index 0 and 1) ---")
print(df.loc[[0, 1]])

print("\n--- First 5 Rows (Head) ---")
print(df.head())

print("\n--- Last 5 Rows (Tail) ---")
print(df.tail())

print("\n--- Checking for Null Values ---")
print(df.isnull())

print("\n--- DataFrame Information ---")
df.info()