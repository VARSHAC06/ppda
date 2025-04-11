import pandas as pd

df = pd.read_csv('experience-data.csv')
print("First 3 rows of the dataframe:")
print(df.head(3))
print("Last 3 rows of the dataframe:")
print(df.tail(3))
print("Description of the dataframe:")
print(df.describe())
print("Information of the dataframe:")
print(df.info())
print("Column names:", df.columns.tolist())
print("Number of columns:", len(df.columns))
