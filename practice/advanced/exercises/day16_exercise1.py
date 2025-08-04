# day16_exercise1.py

# Exercise 1: Advanced Collections

from collections import OrderedDict, ChainMap, UserDict, UserList, Counter

# 1. Compare OrderedDict with regular dict behavior



# 2. Use ChainMap to combine multiple configuration dictionaries
default_config = {'host': 'localhost', 'port': 8080, 'debug': False}
user_config = {'port': 3000, 'debug': True}
env_config = {'host': 'production.server.com'}



# 3. Create custom dictionary class inheriting from UserDict



# 4. Advanced Counter operations for text analysis
text = """
Python is a high-level, interpreted programming language with dynamic semantics.
Its high-level built in data structures, combined with dynamic typing and dynamic binding,
make it very attractive for Rapid Application Development, as well as for use as a
scripting or glue language to connect existing components together.
"""



# Test the advanced collections
if __name__ == "__main__":
    # Test OrderedDict vs regular dict
    print("Testing OrderedDict vs regular dict:")
    test_ordered_dict()
    
    # Test ChainMap
    print("\nTesting ChainMap:")
    test_chainmap()
    
    # Test custom dictionary
    print("\nTesting custom dictionary:")
    custom_dict = CaseInsensitiveDict()
    custom_dict['Name'] = 'John'
    print(custom_dict['name'])  # Should work
    
    # Test advanced Counter operations
    print("\nTesting advanced Counter operations:")
    test_counter_operations()

