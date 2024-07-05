
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

"""
Step 2. Test ensures generate_prime_factors returns an empty list
when it is called with a integer value of 1 argument.
"""
def test_generate_prime_factors_called_with_1_empty_list_returned():
    my_test_null_list = []
    assert my_test_null_list == prime.generate_prime_factors(1)
"""
    Step 3. Test ensures generate_prime_factors returns the [2] list
    when it is called with a integer value of 2 argument.
"""
def test_generate_prime_factors_called_with_2_list_with_2_returned():
    my_test_list = [2]
    assert my_test_list == prime.generate_prime_factors(2)


"""
Step 4. Test ensures generate_prime_factors returns the [3] list
when it is called with a integer value of 3 argument.
"""


def test_generate_prime_factors_called_with_3_list_with_3_returned():
    my_test_list = [3]
    assert my_test_list == prime.generate_prime_factors(3)

"""
Step 5. Test ensures generate_prime_factors returns the [2, 2] list
when it is called with a integer value of 4 argument.
"""


def test_generate_prime_factors_called_with_4_list_with_2_2_returned():
    my_test_list = [2, 2]
    assert my_test_list == prime.generate_prime_factors(4)


"""
Step 6. Test ensures generate_prime_factors returns the [2, 3] list
when it is called with a integer value of 6 argument.
"""


def test_generate_prime_factors_called_with_6_list_with_2_3_returned():
    my_test_list = [2, 3]
    assert my_test_list == prime.generate_prime_factors(6)

"""
Step 7. Test ensures generate_prime_factors returns the [2, 2, 2] list
when it is called with a integer value of 8 argument.
"""


def test_generate_prime_factors_called_with_8_list_with_2_2_2_returned():
    my_test_list = [2, 2, 2]
    assert my_test_list == prime.generate_prime_factors(8)

"""
Step 8. Test ensures generate_prime_factors returns the [3, 3] list
when it is called with a integer value of 9 argument.
"""


def test_generate_prime_factors_called_with_9_list_with_3_3_returned():
    my_test_list = [3, 3]
    assert my_test_list == prime.generate_prime_factors(9)
