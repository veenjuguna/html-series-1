import pandas as pd
df = pd.read_csv('housing_data.csv')
print(df.info())  # Check for missing values and data types
print(df.head())  # Preview the data