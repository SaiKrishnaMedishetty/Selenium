import pandas as pd

# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [24, 27, 22, 32, 29],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}

df = pd.DataFrame(data)

# Specify the path where you want to save the CSV file
file_path = 'Downloads'

# Save the DataFrame to a CSV file
df.to_csv(file_path, index=False)

print(f"CSV file has been generated and saved to {file_path}")
