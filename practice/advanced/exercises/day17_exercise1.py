# day17_exercise1.py

# Exercise 1: Sorting Algorithms

import time
import random

# 1. Implement bubble sort with time complexity analysis



# 2. Implement selection sort and compare with bubble sort



# 3. Implement insertion sort for small datasets



# 4. Implement merge sort using divide and conquer



# 5. Implement quick sort with different pivot strategies



# Test the sorting algorithms
if __name__ == "__main__":
    # Generate test data
    test_sizes = [100, 500, 1000]
    
    for size in test_sizes:
        print(f"\nTesting with {size} elements:")
        
        # Generate random data
        data = [random.randint(1, 1000) for _ in range(size)]
        
        # Test each sorting algorithm
        algorithms = [
            ("Bubble Sort", bubble_sort),
            ("Selection Sort", selection_sort),
            ("Insertion Sort", insertion_sort),
            ("Merge Sort", merge_sort),
            ("Quick Sort", quick_sort)
        ]
        
        for name, algorithm in algorithms:
            test_data = data.copy()
            start_time = time.time()
            sorted_data = algorithm(test_data)
            end_time = time.time()
            
            # Verify sorting is correct
            is_sorted = all(sorted_data[i] <= sorted_data[i+1] for i in range(len(sorted_data)-1))
            
            print(f"{name}: {end_time - start_time:.4f}s, Correct: {is_sorted}")
    
    # Test with different data distributions
    print("\nTesting with different data distributions:")
    size = 1000
    
    # Already sorted data
    sorted_data = list(range(size))
    # Reverse sorted data
    reverse_data = list(range(size, 0, -1))
    # Random data
    random_data = [random.randint(1, 1000) for _ in range(size)]
    
    distributions = [
        ("Sorted", sorted_data),
        ("Reverse", reverse_data),
        ("Random", random_data)
    ]
    
    for dist_name, data in distributions:
        print(f"\n{dist_name} data:")
        for name, algorithm in algorithms[:3]:  # Test first 3 algorithms
            test_data = data.copy()
            start_time = time.time()
            algorithm(test_data)
            end_time = time.time()
            print(f"  {name}: {end_time - start_time:.4f}s")

