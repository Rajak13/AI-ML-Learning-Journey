import pandas as pd

# pandas_example.py

# Importing pandas library

# Creating a DataFrame
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32],
    'City': ['New York', 'Paris', 'Berlin', 'London']
}

df = pd.DataFrame(data)

# Displaying the DataFrame
print("DataFrame:")
print(df)

# Reading data from a CSV file
# df = pd.read_csv('file_path.csv')

# Writing data to a CSV file
# df.to_csv('output_file.csv', index=False)

# Viewing the first few rows of the DataFrame
print("\nFirst 2 rows:")
print(df.head(2))

# Viewing the last few rows of the DataFrame
print("\nLast 2 rows:")
print(df.tail(2))

# Getting basic information about the DataFrame
print("\nDataFrame Info:")
print(df.info())

# Descriptive statistics
print("\nDescriptive Statistics:")
print(df.describe())

# Selecting a single column
print("\nSelecting 'Name' column:")
print(df['Name'])

# Selecting multiple columns
print("\nSelecting 'Name' and 'Age' columns:")
print(df[['Name', 'Age']])

# Filtering rows based on a condition
print("\nFiltering rows where Age > 30:")
print(df[df['Age'] > 30])

# Adding a new column
df['Country'] = ['USA', 'France', 'Germany', 'UK']
print("\nDataFrame after adding 'Country' column:")
print(df)

# Removing a column
df = df.drop(columns=['Country'])
print("\nDataFrame after removing 'Country' column:")
print(df)

# Grouping data
grouped = df.groupby('City').mean()
print("\nGrouped Data by 'City':")
print(grouped)

# Merging DataFrames
data2 = {
    'City': ['New York', 'Paris', 'Berlin', 'London'],
    'Population': [8000000, 2141000, 3769000, 8900000]
}
df2 = pd.DataFrame(data2)
merged_df = pd.merge(df, df2, on='City')
print("\nMerged DataFrame:")
print(merged_df)

# Handling missing data
df_with_nan = df.copy()
df_with_nan.loc[1, 'Age'] = None
print("\nDataFrame with NaN value:")
print(df_with_nan)

# Filling missing data
df_filled = df_with_nan.fillna(0)
print("\nDataFrame after filling NaN values with 0:")
print(df_filled)

# Dropping rows with missing data
df_dropped = df_with_nan.dropna()
print("\nDataFrame after dropping rows with NaN values:")
print(df_dropped)
