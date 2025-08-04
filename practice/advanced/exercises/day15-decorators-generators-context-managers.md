# Day 15: Decorators, Generators, and Context Managers

## Objective

This day delves into advanced Python concepts that enable more elegant, efficient, and Pythonic code: decorators, generators, and context managers. You will learn how to use these features to write cleaner, more reusable, and resource-efficient code, with GitHub Copilot assisting in understanding and implementing them.

## Exercises

### Exercise 1: Decorators

Decorators allow you to modify or enhance functions or methods without changing their source code. Use Copilot to help you implement the following:

1.  **Simple Timer Decorator**: Create a decorator that measures the execution time of a function.
    -   *Prompting Hint*: `# Create a decorator to time function execution`
2.  **Logger Decorator**: Create a decorator that logs the arguments and return value of a function.
    -   *Prompting Hint*: `# Create a decorator to log function calls`
3.  **Authentication Decorator**: Create a decorator that checks if a user is authenticated before allowing access to a function.
    -   *Prompting Hint*: `# Create an authentication decorator`
4.  **Decorator with Arguments**: Create a decorator that takes arguments (e.g., a `retry` decorator that retries a function a specified number of times).
    -   *Prompting Hint*: `# Create a retry decorator that takes max_retries as argument`
5.  **Class Decorator**: Create a class decorator that adds a method to a class.
    -   *Prompting Hint*: `# Create a class decorator to add a method`

### Exercise 2: Generators

Generators are functions that return an iterator, allowing you to iterate over a sequence of values without storing the entire sequence in memory. They are memory-efficient for large datasets.

1.  **Simple Range Generator**: Create a generator that yields numbers in a given range.
    -   *Prompting Hint*: `# Create a generator for a range of numbers`
2.  **Fibonacci Sequence Generator**: Create a generator that yields the Fibonacci sequence up to a certain limit.
    -   *Prompting Hint*: `# Create a generator for Fibonacci sequence`
3.  **Infinite Sequence Generator**: Create a generator that yields an infinite sequence (e.g., even numbers).
    -   *Prompting Hint*: `# Create an infinite generator for even numbers`
4.  **File Line Reader Generator**: Create a generator that reads a large file line by line, yielding each line.
    -   *Prompting Hint*: `# Create a generator to read a file line by line`
5.  **Generator Expression**: Convert a list comprehension into a generator expression.
    -   *Prompting Hint*: `# Convert list comprehension to generator expression`

### Exercise 3: Context Managers

Context managers allow you to allocate and release resources precisely when you want to. The `with` statement is used to ensure that setup and teardown actions are performed.

1.  **Simple File Context Manager**: Create a context manager for handling file operations (opening and closing).
    -   *Prompting Hint*: `# Create a context manager for file handling`
2.  **Timer Context Manager**: Create a context manager that measures the time taken by a block of code.
    -   *Prompting Hint*: `# Create a context manager to time a code block`
3.  **Database Connection Context Manager**: Create a context manager for managing a database connection (connecting and closing).
    -   *Prompting Hint*: `# Create a context manager for database connection`
4.  **Suppress Exceptions Context Manager**: Create a context manager that suppresses specified exceptions within its block.
    -   *Prompting Hint*: `# Create a context manager to suppress exceptions`
5.  **Custom Context Manager with `contextlib`**: Use the `@contextlib.contextmanager` decorator to create a simple context manager.
    -   *Prompting Hint*: `# Use contextlib.contextmanager to create a context manager`

## Challenge Exercise: Data Stream Processor

Combine decorators, generators, and context managers to create a data stream processor:

-   Create a generator that simulates reading data from a sensor (e.g., yielding random temperature readings every second).
-   Create a decorator that filters out invalid readings (e.g., temperatures outside a certain range).
-   Create a context manager that logs the start and end of the data processing session.
-   Use these components together to process a stream of sensor data.

*Prompting Hint*: `# Create a data stream processor using generator, decorator, and context manager`

## Reflection

-   How did Copilot assist you in understanding the syntax and application of decorators, generators, and context managers?
-   Were there any specific patterns Copilot suggested for creating these advanced constructs?
-   How did these concepts change your perspective on writing Pythonic code?

