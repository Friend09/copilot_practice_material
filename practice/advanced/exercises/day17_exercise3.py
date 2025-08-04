# day17_exercise3.py

# Exercise 3: Dynamic Programming

# 1. Implement Fibonacci with memoization



# 2. Implement longest common subsequence using DP



# 3. Solve 0/1 knapsack problem with dynamic programming



# 4. Solve coin change problem with minimum coins



# 5. Calculate edit distance between two strings



# Test the dynamic programming algorithms
if __name__ == "__main__":
    print("Testing Dynamic Programming Algorithms:")
    
    # Test Fibonacci with memoization
    print("\n1. Fibonacci with Memoization:")
    n = 40
    import time
    
    # Compare with naive recursive approach
    def fibonacci_naive(n):
        if n <= 1:
            return n
        return fibonacci_naive(n-1) + fibonacci_naive(n-2)
    
    # Test memoized version
    start_time = time.time()
    result_memo = fibonacci_memoized(n)
    memo_time = time.time() - start_time
    
    # Test naive version (smaller n to avoid long wait)
    start_time = time.time()
    result_naive = fibonacci_naive(min(n, 35))
    naive_time = time.time() - start_time
    
    print(f"Fibonacci({n}) memoized: {result_memo} in {memo_time:.4f}s")
    print(f"Fibonacci({min(n, 35)}) naive: {result_naive} in {naive_time:.4f}s")
    
    # Test Longest Common Subsequence
    print("\n2. Longest Common Subsequence:")
    str1 = "ABCDGH"
    str2 = "AEDFHR"
    lcs_result = longest_common_subsequence(str1, str2)
    print(f"LCS of '{str1}' and '{str2}': length {lcs_result}")
    
    # Test Knapsack Problem
    print("\n3. 0/1 Knapsack Problem:")
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 50
    knapsack_result = knapsack_01(weights, values, capacity)
    print(f"Maximum value with capacity {capacity}: {knapsack_result}")
    
    # Test Coin Change Problem
    print("\n4. Coin Change Problem:")
    coins = [1, 3, 4]
    amount = 6
    coin_change_result = coin_change_min(coins, amount)
    print(f"Minimum coins needed for amount {amount}: {coin_change_result}")
    
    # Test Edit Distance
    print("\n5. Edit Distance:")
    word1 = "kitten"
    word2 = "sitting"
    edit_dist = edit_distance(word1, word2)
    print(f"Edit distance between '{word1}' and '{word2}': {edit_dist}")

