# day16_exercise4.py

# Exercise 4: Real-World Applications

from collections import OrderedDict
import heapq

# 1. Implement LRU cache using OrderedDict



# 2. Implement graph with adjacency list and matrix



# 3. Implement priority queue using heapq



# 4. Implement a trie for string prefix matching



# Test the real-world applications
if __name__ == "__main__":
    # Test LRU Cache
    print("Testing LRU Cache:")
    cache = LRUCache(3)
    cache.put(1, "A")
    cache.put(2, "B")
    cache.put(3, "C")
    print(cache.get(1)) # Access 1, makes it most recently used
    cache.put(4, "D") # 2 should be evicted
    print(cache.get(2)) # Should be -1
    
    # Test Graph
    print("\nTesting Graph:")
    graph = Graph(5)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    print("Adjacency List:")
    graph.print_adj_list()
    print("Adjacency Matrix:")
    graph.print_adj_matrix()
    
    # Test Priority Queue
    print("\nTesting Priority Queue:")
    pq = PriorityQueue()
    pq.push("task1", 3)
    pq.push("task2", 1)
    pq.push("task3", 2)
    print(pq.pop())
    print(pq.pop())
    
    # Test Trie
    print("\nTesting Trie:")
    trie = Trie()
    words = ["apple", "apricot", "apply", "banana"]
    for word in words:
        trie.insert(word)
    print(trie.search("apple"))
    print(trie.search("app"))
    print(trie.starts_with("app"))
    print(trie.starts_with("ban"))
    print(trie.search("grape"))

