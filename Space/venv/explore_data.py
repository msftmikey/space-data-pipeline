import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv("asteroid_data.csv")

# Display the first few rows of the data
print(df.head())

# Basic statistics about the numerical columns
print(df.describe())

# Check for missing values
print(df.isnull().sum())
