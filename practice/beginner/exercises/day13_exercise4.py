# day13_exercise4.py

# Exercise 4: Data Visualization Preparation

import csv
import math
from collections import defaultdict

# Sample data with more variety for analysis
analysis_data = [
    ['Name', 'Age', 'Salary', 'Department', 'Years_Experience'],
    ['John Smith', '30', '75000', 'Engineering', '5'],
    ['Jane Doe', '25', '65000', 'Marketing', '3'],
    ['Bob Johnson', '35', '70000', 'Sales', '8'],
    ['Alice Brown', '28', '80000', 'Engineering', '4'],
    ['Charlie Wilson', '32', '72000', 'Sales', '6'],
    ['Diana Prince', '29', '68000', 'Marketing', '4'],
    ['Eve Adams', '26', '78000', 'Engineering', '3'],
    ['Frank Miller', '38', '85000', 'Sales', '12'],
]

# Write sample data to file
with open('employee_analysis.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(analysis_data)

# 1. Generate summary statistics for CSV data



# 2. Create frequency distribution for categorical data



# 3. Group numeric data into bins (age groups)



# 4. Calculate correlation between two numeric columns



# Challenge: Comprehensive sales data analysis
# Use the sales data from previous exercise for comprehensive analysis

