# day15_exercise2.py

# Exercise 2: Generators

# 1. Create a generator for a range of numbers



# 2. Create a generator for Fibonacci sequence



# 3. Create an infinite generator for even numbers



# 4. Create a generator to read a file line by line
# First create a sample file
sample_text = """Line 1: This is the first line
Line 2: This is the second line
Line 3: This is the third line
Line 4: This is the fourth line
Line 5: This is the fifth line"""

with open('sample_file.txt', 'w') as f:
    f.write(sample_text)



# 5. Convert list comprehension to generator expression
# Original list comprehension: squares = [x**2 for x in range(10)]



# Test the generators
if __name__ == "__main__":
    # Test range generator
    print("Range generator:")
    for num in number_range(1, 5):
        print(num)
    
    # Test Fibonacci generator
    print("\nFibonacci generator:")
    for fib in fibonacci_sequence(50):
        print(fib)
    
    # Test infinite even numbers (limited to first 10)
    print("\nInfinite even numbers (first 10):")
    even_gen = infinite_even_numbers()
    for _ in range(10):
        print(next(even_gen))
    
    # Test file reader generator
    print("\nFile reader generator:")
    for line in read_file_lines('sample_file.txt'):
        print(line.strip())
    
    # Test generator expression
    print("\nGenerator expression:")
    for square in squares_gen:
        print(square)

