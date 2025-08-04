# Day 11: Libraries and Data Manipulation

## Objective

This day focuses on using common Python libraries for data manipulation, particularly `collections` and `datetime`, and basic data processing techniques. You will learn how to leverage these libraries to efficiently handle and transform data, with GitHub Copilot assisting in generating the necessary code.

## Exercises

### Exercise 1: Using the `collections` Module

The `collections` module provides specialized container datatypes. Use Copilot to help you implement the following tasks:

1.  **`Counter`**: Count the frequency of words in a given sentence.
    -   *Prompting Hint*: `# Use collections.Counter to count word frequency in a string`
2.  **`defaultdict`**: Group a list of dictionaries by a specific key.
    -   *Prompting Hint*: `# Group a list of dictionaries by 'category' using defaultdict`
3.  **`namedtuple`**: Define a simple `Point` namedtuple with `x` and `y` coordinates, and create an instance.
    -   *Prompting Hint*: `# Define a namedtuple for a 2D point`
4.  **`deque`**: Implement a basic queue using `deque` and demonstrate adding and removing elements from both ends.
    -   *Prompting Hint*: `# Implement a queue using collections.deque`

### Exercise 2: Working with `datetime`

The `datetime` module supplies classes for working with dates and times. Use Copilot to assist with these tasks:

1.  **Current Date and Time**: Get and print the current date and time.
    -   *Prompting Hint*: `# Get current date and time`
2.  **Formatting Dates**: Format a given `datetime` object into a specific string format (e.g., "YYYY-MM-DD HH:MM:SS").
    -   *Prompting Hint*: `# Format datetime object to 'YYYY-MM-DD HH:MM:SS'`
3.  **Parsing Dates**: Parse a date string (e.g., "2023-10-27 14:30:00") into a `datetime` object.
    -   *Prompting Hint*: `# Parse date string '2023-10-27 14:30:00' into datetime object`
4.  **Date Arithmetic**: Calculate the difference between two dates (e.g., how many days until a specific event).
    -   *Prompting Hint*: `# Calculate days remaining until a future date`
5.  **Time Zones**: Convert a `datetime` object from UTC to a specific time zone (e.g., 'America/New_York').
    -   *Prompting Hint*: `# Convert UTC datetime to 'America/New_York' timezone`

### Exercise 3: Basic Data Processing

Apply your knowledge of data structures and libraries to perform basic data processing tasks.

1.  **Filtering Data**: Given a list of dictionaries representing products (with keys like `name`, `price`, `category`), filter out products belonging to a specific category.
    -   *Prompting Hint*: `# Filter products by category 'Electronics'`
2.  **Aggregating Data**: Calculate the total price of all products in a list of dictionaries.
    -   *Prompting Hint*: `# Calculate total price of products in a list of dictionaries`
3.  **Sorting Data**: Sort the list of products by price in ascending order.
    -   *Prompting Hint*: `# Sort products by price ascending`
4.  **Data Transformation**: Convert a list of Fahrenheit temperatures to Celsius.
    -   *Prompting Hint*: `# Convert list of Fahrenheit temperatures to Celsius`

## Challenge Exercise: Log File Analysis

Imagine you have a simple log file where each line contains a timestamp and a message (e.g., `2023-10-27 10:00:05 - INFO: User logged in`).

-   Write a Python script that reads this log file.
-   Count the number of `INFO`, `WARNING`, and `ERROR` messages.
-   Identify the busiest hour (the hour with the most log entries).
-   *Prompting Hint*: `# Analyze log file for message types and busiest hour`

## Reflection

-   How did Copilot assist you in understanding and using the `collections` and `datetime` modules?
-   Were there any specific prompts that yielded particularly good results for data manipulation tasks?
-   How did Copilot help you structure the log file analysis challenge?

