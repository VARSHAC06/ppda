import pandas as pd

file_path = 'employees.csv'
df = pd.read_csv(file_path)
print("Shape of the DataFrame:", df.shape)
print("Total Rows:", len(df))
print("Total Columns:", len(df.columns))
print("Length of the DataFrame (number of rows):", len(df))
print("Number of dimensions of the DataFrame:", df.ndim)
print("First 5 rows of the DataFrame:")
print(df.head())
print("Information about the DataFrame:")
print(df.info())
