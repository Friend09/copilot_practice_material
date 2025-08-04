# day17_exercise2.py

# Exercise 2: Searching Algorithms

from collections import deque

# 1. Implement linear search for unsorted arrays



# 2. Implement binary search iterative and recursive



# 3. Binary search variations for first/last occurrence



# 4. Implement DFS for graph traversal



# 5. Implement BFS for shortest path in unweighted graph



# Test the searching algorithms
if __name__ == "__main__":
    # Test linear and binary search
    print("Testing Search Algorithms:")
    
    # Test data
    unsorted_array = [64, 34, 25, 12, 22, 11, 90, 5]
    sorted_array = [5, 11, 12, 22, 25, 34, 64, 90]
    target = 22
    
    # Linear search
    linear_result = linear_search(unsorted_array, target)
    print(f"Linear search for {target}: index {linear_result}")
    
    # Binary search
    binary_iter_result = binary_search_iterative(sorted_array, target)
    binary_rec_result = binary_search_recursive(sorted_array, target, 0, len(sorted_array) - 1)
    print(f"Binary search iterative for {target}: index {binary_iter_result}")
    print(f"Binary search recursive for {target}: index {binary_rec_result}")
    
    # Binary search variations
    array_with_duplicates = [1, 2, 2, 2, 3, 4, 4, 5]
    target_dup = 2
    first_occurrence = find_first_occurrence(array_with_duplicates, target_dup)
    last_occurrence = find_last_occurrence(array_with_duplicates, target_dup)
    print(f"First occurrence of {target_dup}: index {first_occurrence}")
    print(f"Last occurrence of {target_dup}: index {last_occurrence}")
    
    # Test graph traversal
    print("\nTesting Graph Traversal:")
    
    # Create a sample graph
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    
    print("DFS traversal starting from A:")
    dfs_result = dfs(graph, 'A')
    print(dfs_result)
    
    print("BFS traversal starting from A:")
    bfs_result = bfs(graph, 'A')
    print(bfs_result)
    
    print("Shortest path from A to F:")
    shortest_path = bfs_shortest_path(graph, 'A', 'F')
    print(shortest_path)

