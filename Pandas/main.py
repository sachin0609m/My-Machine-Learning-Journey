import pandas as pd

# Series 
df = pd.Series([10, 20, 30, 40, 50], index=['sachin', 'nupur', 'parth', 'priya', 'aditi'])
print(df)
print(df['sachin'])  # Output: 10
print(df.mean())  # Output: 30.0

# ------------------------------------------------------------------------------------
# DataFrame
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
# Read CSV file
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

# -------------------------------------------------------------------------------
d = pd.read_csv('students_raw.csv')

marked = d['prev_marks'] > 70
print(marked)  # Output: Series of boolean values indicating whether 'prev_marks' is greater than 70
print(d[marked])  # Output: DataFrame with rows where 'prev_marks' is greater than 70

top_students = d[d['prev_marks'] > 70]
print(top_students)  # Output: DataFrame with rows where 'prev_marks' is greater than 70
print(d[d['prev_marks'] > 70])  # Output: DataFrame with rows where 'prev_marks' is greater than 70

p = d["passed"] == 1
print('passed',p.sum())  
# print(d[paa]) 
f = d["passed"] == 0
print('failed',f.sum()) 

df = d.columns
print(df)  # Output: List of column names in the DataFrame

print((d["hours_studied"] >8).sum())  # Output: Count of rows where 'passed' is equal to 1


