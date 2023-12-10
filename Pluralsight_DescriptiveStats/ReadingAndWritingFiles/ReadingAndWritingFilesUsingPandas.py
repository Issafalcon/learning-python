import pandas as pd
import numpy as np

print('Pandas Version:')
print(pd.__version__)

print('NumPy Version:')
print(np.__version__)

# Import Customer Data
mall_data = pd.read_json('./Mall_Customers.json')

print(mall_data.head())

# Calculate mean income
average_income = mall_data['annual_income'].mean()
print(average_income)

# Add new column to dataframe
mall_data['above_average_income'] = (mall_data['annual_income'] - average_income) > 0
print(mall_data.sample(5))

mall_data.to_csv('./Mall_Customers_Processed.csv', index=False)
