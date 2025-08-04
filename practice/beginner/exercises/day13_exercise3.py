# day13_exercise3.py

# Exercise 3: Basic Data Analysis

import csv
from collections import defaultdict, Counter

# Sample sales data
sales_data = [
    ['Date', 'Product', 'Category', 'Quantity', 'Price', 'Salesperson'],
    ['2023-01-15', 'Laptop', 'Electronics', '2', '999.99', 'John Smith'],
    ['2023-01-16', 'Book', 'Education', '5', '25.50', 'Jane Doe'],
    ['2023-01-17', 'Phone', 'Electronics', '1', '699.00', 'John Smith'],
    ['2023-01-18', 'Notebook', 'Education', '10', '5.99', 'Bob Johnson'],
    ['2023-01-19', 'Tablet', 'Electronics', '3', '399.99', 'Jane Doe'],
    ['2023-01-20', 'Laptop', 'Electronics', '1', '999.99', 'Bob Johnson'],
    ['2023-01-21', 'Book', 'Education', '3', '25.50', 'John Smith'],
]

# Write sample data to file
with open('sales_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(sales_data)

# 1. Calculate average of numeric column in CSV



# 2. Find min and max values in CSV column



# 3. Count unique values in CSV column



# 4. Group CSV data by category and calculate aggregates



# 5. Sort CSV data by multiple columns

