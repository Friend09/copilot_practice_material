# Day 13: CSV Processing and Basic Data Analysis

## Objective

Today focuses on working with CSV files and performing basic data analysis using Python's built-in `csv` module and basic statistical operations. You will learn how to read, write, and manipulate CSV data, with GitHub Copilot assisting in generating the necessary code.

## Exercises

### Exercise 1: Reading and Writing CSV Files

Learn the fundamentals of CSV file operations.

1.  **Read CSV File**: Read a CSV file and print its contents.
    -   *Prompting Hint*: `# Read CSV file and print contents`
2.  **Write CSV File**: Create a new CSV file with sample data (e.g., employee information).
    -   *Prompting Hint*: `# Write employee data to CSV file`
3.  **CSV with Headers**: Read a CSV file that includes headers and access data by column name.
    -   *Prompting Hint*: `# Read CSV with headers using DictReader`
4.  **Append to CSV**: Append new rows to an existing CSV file.
    -   *Prompting Hint*: `# Append new rows to existing CSV file`
5.  **Handle Different Delimiters**: Read a CSV file that uses semicolons (;) as delimiters instead of commas.
    -   *Prompting Hint*: `# Read CSV file with semicolon delimiter`

### Exercise 2: Data Cleaning and Preprocessing

Practice cleaning and preprocessing CSV data.

1.  **Remove Empty Rows**: Filter out rows that contain empty or null values.
    -   *Prompting Hint*: `# Remove rows with empty values from CSV data`
2.  **Data Type Conversion**: Convert string numbers to integers or floats.
    -   *Prompting Hint*: `# Convert string numbers to appropriate data types`
3.  **Standardize Text**: Convert all text data to lowercase and strip whitespace.
    -   *Prompting Hint*: `# Standardize text data in CSV`
4.  **Handle Missing Data**: Replace missing values with default values or averages.
    -   *Prompting Hint*: `# Handle missing values in CSV data`
5.  **Remove Duplicates**: Identify and remove duplicate rows from CSV data.
    -   *Prompting Hint*: `# Remove duplicate rows from CSV data`

### Exercise 3: Basic Data Analysis

Perform basic statistical analysis on CSV data.

1.  **Calculate Averages**: Calculate the average of a numeric column.
    -   *Prompting Hint*: `# Calculate average of numeric column in CSV`
2.  **Find Min/Max Values**: Find the minimum and maximum values in a column.
    -   *Prompting Hint*: `# Find min and max values in CSV column`
3.  **Count Occurrences**: Count how many times each unique value appears in a column.
    -   *Prompting Hint*: `# Count unique values in CSV column`
4.  **Group and Aggregate**: Group data by a category and calculate aggregates (sum, average, count).
    -   *Prompting Hint*: `# Group CSV data by category and calculate aggregates`
5.  **Sort Data**: Sort CSV data by one or more columns.
    -   *Prompting Hint*: `# Sort CSV data by multiple columns`

### Exercise 4: Data Visualization Preparation

Prepare data for visualization (without actually creating charts).

1.  **Create Summary Statistics**: Generate a summary report with key statistics for numeric columns.
    -   *Prompting Hint*: `# Generate summary statistics for CSV data`
2.  **Frequency Distribution**: Create a frequency distribution for categorical data.
    -   *Prompting Hint*: `# Create frequency distribution for categorical data`
3.  **Data Binning**: Group numeric data into bins (e.g., age groups: 0-18, 19-35, 36-65, 65+).
    -   *Prompting Hint*: `# Group numeric data into bins`
4.  **Correlation Analysis**: Calculate correlation between two numeric columns.
    -   *Prompting Hint*: `# Calculate correlation between two numeric columns`

## Challenge Exercise: Sales Data Analysis

You have a CSV file containing sales data with columns: `date`, `product`, `category`, `quantity`, `price`, `salesperson`.

Create a comprehensive analysis that:
-   Calculates total revenue by product and category
-   Identifies the top-performing salesperson
-   Finds the best-selling product
-   Analyzes sales trends by month
-   Generates a summary report

*Prompting Hint*: `# Comprehensive sales data analysis with revenue, trends, and performance metrics`

## Sample Data

Create a sample CSV file with the following structure for testing:

```csv
date,product,category,quantity,price,salesperson
2023-01-15,Laptop,Electronics,2,999.99,John Smith
2023-01-16,Book,Education,5,25.50,Jane Doe
2023-01-17,Phone,Electronics,1,699.00,John Smith
2023-01-18,Notebook,Education,10,5.99,Bob Johnson
2023-01-19,Tablet,Electronics,3,399.99,Jane Doe
```

## Reflection

-   How did Copilot assist you in handling different CSV formats and delimiters?
-   Were there any specific patterns Copilot suggested for data cleaning operations?
-   How effective was Copilot in helping you perform statistical calculations on CSV data?

