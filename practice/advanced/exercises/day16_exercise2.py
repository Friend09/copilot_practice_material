# day16_exercise2.py

# Exercise 2: Custom Data Structures

from collections import deque

# 1. Implement a stack data structure with basic operations



# 2. Implement a queue data structure using deque



# 3. Implement a singly linked list with basic operations



# 4. Implement a binary tree with insert and traversal



# 5. Implement a hash table with collision handling



# Test the custom data structures
if __name__ == "__main__":
    # Test Stack
    print("Testing Stack:")
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f"Peek: {stack.peek()}")
    print(f"Pop: {stack.pop()}")
    print(f"Is empty: {stack.is_empty()}")
    
    # Test Queue
    print("\nTesting Queue:")
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(f"Dequeue: {queue.dequeue()}")
    print(f"Is empty: {queue.is_empty()}")
    
    # Test Linked List
    print("\nTesting Linked List:")
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    print(f"Search 2: {ll.search(2)}")
    ll.delete(2)
    print(f"Search 2 after delete: {ll.search(2)}")
    
    # Test Binary Tree
    print("\nTesting Binary Tree:")
    bt = BinaryTree()
    bt.insert(5)
    bt.insert(3)
    bt.insert(7)
    bt.insert(1)
    bt.insert(9)
    print("Inorder traversal:")
    bt.inorder_traversal()
    
    # Test Hash Table
    print("\nTesting Hash Table:")
    ht = HashTable()
    ht.put("key1", "value1")
    ht.put("key2", "value2")
    print(f"Get key1: {ht.get('key1')}")
    ht.remove("key1")
    print(f"Get key1 after remove: {ht.get('key1')}")

