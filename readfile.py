import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
file_path = r'C:\Users\smedishetty1\Downloads\sample\synthetic_iot_network_traffic.csv'
try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    print(f"File not found: {file_path}")
    exit()

# Display the first few rows of the DataFrame
print("First few rows of the DataFrame:")
print(df.head())

# Display summary statistics
print("\nSummary statistics:")
print(df.describe())

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# Plot histograms for numerical columns
df.hist(figsize=(10, 8))
plt.suptitle('Histograms of Numerical Columns')
plt.show()

# Plot a bar chart for a categorical column (if any)
# Here we assume 'Category' is a placeholder for any categorical column you have
# Replace 'Category' with your actual categorical column name
categorical_column = 'Category'
if categorical_column in df.columns:
    if df[categorical_column].dtype == 'object' or df[categorical_column].dtype.name == 'category':
        df[categorical_column].value_counts().plot(kind='bar')
        plt.title(f'Bar Chart of {categorical_column}')
        plt.xlabel(categorical_column)
        plt.ylabel('Count')
        plt.show()
    else:
        print(f"Column '{categorical_column}' is not a categorical column.")
else:
    print(f"Categorical column '{categorical_column}' not found in DataFrame.")
