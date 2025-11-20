---
title: Comprehensive Test Generation
description: Generate complete test suite with unit, integration, and edge case tests
tags: [testing, pytest, unit-tests, integration-tests]
---

# Test Generation Prompt

Generate comprehensive tests for the selected code.

## Test Requirements

### 1. Unit Tests
- Test each function/method independently
- Mock external dependencies
- Cover all code paths
- Test return values and side effects

### 2. Edge Cases
- Empty inputs
- Null/None values
- Boundary conditions
- Invalid inputs
- Large datasets
- Unicode and special characters

### 3. Error Conditions
- Expected exceptions
- Error messages
- Error recovery
- Timeout scenarios

### 4. Integration Tests
- Test with real dependencies (where appropriate)
- Database interactions
- API calls
- File system operations

### 5. Performance Tests
- Test with large datasets (if relevant)
- Measure execution time
- Check memory usage

## Test Structure

```python
import pytest
from unittest.mock import Mock, patch

class TestClassName:
    """Test suite for ClassName"""

    @pytest.fixture
    def setup_data(self):
        """Fixture for common test data"""
        return {}

    def test_function_success_case(self, setup_data):
        """Test successful execution"""
        pass

    def test_function_with_invalid_input(self):
        """Test error handling"""
        with pytest.raises(ValueError):
            pass

    def test_function_edge_case_empty(self):
        """Test with empty input"""
        pass
```

## Coverage Goal

Aim for:
- **90%+ code coverage**
- **All edge cases covered**
- **All error paths tested**
- **Clear test names**
- **Good docstrings**

## Naming Convention

```
test_<function_name>_<scenario>_<expected_result>

Examples:
- test_calculate_total_with_valid_items_returns_sum
- test_validate_email_with_invalid_format_raises_error
- test_process_data_with_empty_list_returns_empty_list
```

## Example Usage

Select function and run:
```
@workspace Use test-generation prompt to create tests for this function
```
