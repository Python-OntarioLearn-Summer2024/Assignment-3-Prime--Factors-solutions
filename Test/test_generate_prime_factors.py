
"""
The test module for prime factors
"""

import pytest
import prime

"""
Step 1. Test ensures generate_prime_factors raises a ValueError
when it is called with a non-integer argument.
"""
def test_data_type_not_integer_value_error_raised():
    my_string = "string"
    my_float = 5.2
    with pytest.raises(ValueError):
        prime.generate_prime_factors(my_string)
    with pytest.raises(ValueError):
        prime.generate_prime_factors(my_float)