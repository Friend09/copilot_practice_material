# Multi-Model Exercise Prompts

Use these prompts to test different models and compare their responses.

## 🎯 Prompt Set 1: Code Generation

### Beginner
```
Create a Python function that checks if a string is a palindrome.
Include edge cases and docstrings.
```

### Intermediate
```
Implement a LRU (Least Recently Used) cache in Python with O(1)
get and put operations. Use appropriate data structures.
```

### Advanced
```
Design and implement a thread-safe connection pool for database
connections. Support timeout, max connections, and graceful shutdown.
Include comprehensive error handling and logging.
```

## 🎯 Prompt Set 2: Code Review

### Code Sample 1 (Simple)
```python
def calc(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b
```

**Prompt:**
```
Review this code and suggest improvements for readability,
error handling, and Pythonic style.
```

### Code Sample 2 (Intermediate)
```python
class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, name, email):
        self.users.append({'name': name, 'email': email})

    def get_user(self, email):
        for user in self.users:
            if user['email'] == email:
                return user
        return None

    def delete_user(self, email):
        for i in range(len(self.users)):
            if self.users[i]['email'] == email:
                del self.users[i]
                return True
        return False
```

**Prompt:**
```
Analyze this code for performance, design patterns, and best practices.
Suggest refactorings to make it production-ready.
```

## 🎯 Prompt Set 3: Algorithm Design

### Problem 1
```
Implement a function to find the longest substring without
repeating characters. Optimize for time complexity.
```

### Problem 2
```
Design an algorithm to serialize and deserialize a binary tree.
The serialization should be compact and efficient.
```

### Problem 3
```
Implement a rate limiter that allows N requests per time window
using the sliding window log algorithm. Must be thread-safe.
```

## 🎯 Prompt Set 4: Architecture & Design

### Scenario 1
```
Design a URL shortener service like bit.ly. Consider:
- Database schema
- API endpoints
- Scalability (millions of URLs)
- Analytics (track clicks)
- Custom short URLs
```

### Scenario 2
```
Architect a real-time notification system for a social media app.
Handle push notifications, email, and SMS. Scale to millions of users.
```

## 🎯 Prompt Set 5: Debugging

### Bug 1
```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# This is very slow for n > 30. Why and how to fix?
```

**Prompt:**
```
Explain why this code is slow and provide an optimized version.
Compare time complexity before and after.
```

### Bug 2
```python
def process_batch(items):
    results = []
    for item in items:
        result = expensive_operation(item)
        results.append(result)
    return results

# This takes 10 seconds for 1000 items. How to optimize?
```

**Prompt:**
```
Identify performance bottlenecks and suggest optimizations.
Consider parallel processing, caching, and async options.
```

## 🎯 Prompt Set 6: Testing

### Test Generation 1
```python
def validate_email(email: str) -> bool:
    """Validate email address format."""
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))
```

**Prompt:**
```
Generate comprehensive pytest tests for this function.
Cover edge cases, invalid inputs, and valid formats.
Aim for 100% code coverage.
```

### Test Generation 2
```python
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item, price, quantity=1):
        self.items.append({
            'item': item,
            'price': price,
            'quantity': quantity
        })

    def total(self):
        return sum(item['price'] * item['quantity'] for item in self.items)

    def apply_discount(self, percentage):
        if not 0 <= percentage <= 100:
            raise ValueError("Invalid discount")
        # Apply discount to total
```

**Prompt:**
```
Create unit tests and integration tests for this shopping cart.
Mock external dependencies. Test error conditions.
```

## 🎯 Prompt Set 7: Documentation

### Code to Document
```python
class TokenBucket:
    def __init__(self, capacity, refill_rate):
        self.capacity = capacity
        self.tokens = capacity
        self.refill_rate = refill_rate
        self.last_refill = time.time()

    def consume(self, tokens=1):
        self._refill()
        if self.tokens >= tokens:
            self.tokens -= tokens
            return True
        return False

    def _refill(self):
        now = time.time()
        elapsed = now - self.last_refill
        refill = elapsed * self.refill_rate
        self.tokens = min(self.capacity, self.tokens + refill)
        self.last_refill = now
```

**Prompt:**
```
Add comprehensive documentation to this class:
- Class docstring with usage examples
- Method docstrings with parameters and returns
- Type hints for all methods
- Inline comments for complex logic
```

## 🎯 Prompt Set 8: Refactoring

### Legacy Code
```python
def process(data):
    r = []
    for d in data:
        if d['type'] == 'A':
            x = d['value'] * 2
            if x > 100:
                r.append({'result': x, 'status': 'high'})
            else:
                r.append({'result': x, 'status': 'low'})
        elif d['type'] == 'B':
            x = d['value'] * 3
            if x > 100:
                r.append({'result': x, 'status': 'high'})
            else:
                r.append({'result': x, 'status': 'low'})
        elif d['type'] == 'C':
            x = d['value'] * 4
            if x > 100:
                r.append({'result': x, 'status': 'high'})
            else:
                r.append({'result': x, 'status': 'low'})
    return r
```

**Prompt:**
```
Refactor this code to be clean, maintainable, and extensible.
Use appropriate design patterns. Add type hints and documentation.
```

## 📊 Evaluation Criteria

When comparing model responses, evaluate:

### Code Quality (1-5 stars)
- ⭐ Correctness
- ⭐ Efficiency
- ⭐ Readability
- ⭐ Error Handling
- ⭐ Documentation

### Response Quality (1-5 stars)
- ⭐ Completeness
- ⭐ Clarity of explanation
- ⭐ Practical usability
- ⭐ Edge case coverage
- ⭐ Best practices adherence

### Speed (1-5 stars)
- ⭐⭐⭐⭐⭐ < 2 seconds
- ⭐⭐⭐⭐ 2-5 seconds
- ⭐⭐⭐ 5-10 seconds
- ⭐⭐ 10-20 seconds
- ⭐ > 20 seconds

## 📝 Recording Template

Use this template to track your experiments:

```
Model: _______________
Prompt: _______________
Response Time: _____ seconds

Quality Ratings:
- Correctness: ⭐⭐⭐⭐⭐
- Efficiency: ⭐⭐⭐⭐⭐
- Readability: ⭐⭐⭐⭐⭐
- Documentation: ⭐⭐⭐⭐⭐
- Overall: ⭐⭐⭐⭐⭐

Notes:
- What I liked:
- What could be better:
- Would I use this model for similar tasks?
```

## 🎓 Learning Goals

After completing these exercises, you should be able to:

1. Identify which model is best for different task types
2. Understand the speed/quality tradeoff
3. Recognize each model's strengths and weaknesses
4. Make informed decisions about model selection
5. Optimize your workflow by switching models strategically
