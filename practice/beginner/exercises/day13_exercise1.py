# day13_exercise1.py

# Exercise 1: Reading and Writing CSV Files

import csv

# Sample data for testing
sample_data = [
    ['Name', 'Age', 'Department', 'Salary'],
    ['John Smith', '30', 'Engineering', '75000'],
    ['Jane Doe', '25', 'Marketing', '65000'],
    ['Bob Johnson', '35', 'Sales', '70000'],
    ['Alice Brown', '28', 'Engineering', '80000']
]

# Create a sample CSV file first
with open('employees.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(sample_data)

# 1. Read CSV file and print contents



# 2. Write employee data to CSV file



# 3. Read CSV with headers using DictReader



# 4. Append new rows to existing CSV file



# 5. Read CSV file with semicolon delimiter
# First create a semicolon-delimited file
semicolon_data = [
    'Name;Age;City',
    'Alice;30;New York',
    'Bob;25;Los Angeles',
    'Charlie;35;Chicago'
]

with open('semicolon_data.csv', 'w') as file:
    for line in semicolon_data:
        file.write(line + '\n')

