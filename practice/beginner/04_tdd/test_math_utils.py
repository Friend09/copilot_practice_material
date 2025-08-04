import pytest
from math_utils import factorial, is_prime

def test_factorial_basic():
    assert factorial(0) == 1
    assert factorial(5) == 120

def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial(-3)

@pytest.mark.parametrize("n,expected", [(2, True), (3, True), (4, False), (17, True)])
def test_is_prime(n, expected):
    assert is_prime(n) == expected
