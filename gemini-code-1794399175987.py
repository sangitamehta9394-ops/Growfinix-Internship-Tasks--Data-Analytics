import pandas as pd
import numpy as np

# 1. Load the raw dataset
df_raw = pd.read_csv('sales_data_raw.csv')

# 2. Drop exact duplicate rows
df_cleaned = df_raw.drop_duplicates().copy()

# 3. Handle negative quantities (correcting anomalies to absolute values)
df_cleaned['Quantity'] = df_cleaned['Quantity'].apply(lambda x: abs(x) if pd.notnull(x) and x < 0 else x)

# 4. Fill missing values in categorical columns
df_cleaned['Customer_Name'] = df_cleaned['Customer_Name'].fillna('Unknown')

# 5. Strip trailing whitespace from text categories
df_cleaned['Category'] = df_cleaned['Category'].fillna('Uncategorized').str.strip()

# 6. Recalculate Total Sales to ensure financial accuracy
df_cleaned['Total_Sales'] = df_cleaned['Quantity'] * df_cleaned['Unit_Price']

# 7. Standardize date format to YYYY-MM-DD
df_cleaned['Date'] = pd.to_datetime(df_cleaned['Date'], errors='coerce').dt.strftime('%Y-%m-%d')
df_cleaned['Date'] = df_cleaned['Date'].fillna('2026-10-14')

# 8. Export the cleaned dataset
df_cleaned.to_csv('sales_data_cleaned.csv', index=False)