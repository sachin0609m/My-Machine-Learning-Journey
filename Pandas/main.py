import pandas as pd

# # Series 

df = pd.Series([10, 20, 30, 40, 50], index=['sachin', 'nupur', 'parth', 'priya', 'aditi'])
print(df)
print(df['sachin'])  # Output: 10
print(df.mean())  # Output: 30.0

# ------------------------------------------------------------------------------------
# # DataFrame
data = {
    'Name': ['sachin', 'nupur', 'parth', 'priya', 'aditi'],
    'Age': [25, 30, 35, 40, 45],
    'City': ['pune', 'mumbai', 'delhi', 'bangalore', 'chennai']
}

df = pd.DataFrame({
    'Name': ['sachin', 'nupur', 'parth', 'priya', 'aditi'],
    'Age': [25, 30, 35, 40, 45],
    'City': ['pune', 'mumbai', 'delhi', 'bangalore', 'chennai']
})

print(df)
print(df.shape)  # Output: (5, 3)
print(df.dtypes) 

# --------------------------------------------------------------------------------
# # Read CSV file
df = pd.read_csv('students_raw.csv')
print(df) 

print(df.head())  # Output: First 5 rows of the DataFrame

print(df.tail())  # Output: Last 5 rows of the DataFrame

print(df.info())  # Output: Summary of the DataFrame 

print(df.describe())  # Output: Statistical summary of the DataFrame

print(df['student_name'])  # Output: Series of the 'Name' column

print(df[['student_name', 'passed']].head())  # Output: DataFrame with the specified columns

print(df.loc[0])  # Output: First row of the DataFrame

print(df.iloc[2])  # Output: Third row of the DataFrame using integer-location based indexing


