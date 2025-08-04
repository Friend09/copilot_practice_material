# day13_exercise2.py

# Exercise 2: Data Cleaning and Preprocessing

import csv

# Sample messy data
messy_data = [
    ['Name', 'Age', 'Salary', 'Department'],
    ['John Smith', '30', '75000', 'Engineering'],
    ['', '25', '65000', 'Marketing'],  # Empty name
    ['Bob Johnson', '', '70000', 'Sales'],  # Empty age
    ['Alice Brown', '28', '', 'Engineering'],  # Empty salary
    ['  Jane Doe  ', '25', '65000', '  Marketing  '],  # Extra whitespace
    ['CHARLIE WILSON', '35', '80000', 'SALES'],  # Uppercase
    ['John Smith', '30', '75000', 'Engineering'],  # Duplicate
]

# Write messy data to file for testing
with open('messy_employees.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(messy_data)

# 1. Remove rows with empty values from CSV data



# 2. Convert string numbers to appropriate data types



# 3. Standardize text data in CSV



# 4. Handle missing values in CSV data



# 5. Remove duplicate rows from CSV data

