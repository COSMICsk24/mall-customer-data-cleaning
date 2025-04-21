import pandas as pd

# Load dataset
df = pd.read_csv("Mall_Customers.csv")

# Show first few rows
print("Preview:\n", df.head())

# Show dataset info
print("\nInitial Info:")
print(df.info())

# Show missing values
print("\nMissing Values:\n", df.isnull().sum())

# Remove duplicates
df = df.drop_duplicates()

# Standardize text in 'Gender'
df['Gender'] = df['Gender'].str.strip().str.capitalize()

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Convert 'age' to int (if needed)
df['age'] = df['age'].astype(int)

# Save cleaned file
df.to_csv("cleaned_mall_customers.csv", index=False)

print("\n✅ Cleaned dataset saved as 'cleaned_mall_customers.csv'")
