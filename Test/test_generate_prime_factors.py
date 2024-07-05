
"""
The test module for prime factors
"""

import pytest
import prime

def generate_prime_factors():
    """
    A test to see a ValueError get raised if the user enters a non-integer data type


    """
    with pytest.raises(ValueError):
        prime.generate_prime_factors(3.14)
    with pytest.rases(ValueError):
        prime.generate_prime_factors("abc")
def test_integer_1_empty_list():
    """
    A test to get an empty list with interger of 1

    """
    assert prime.generate_prime_factors(1) == []