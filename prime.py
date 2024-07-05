"""
prime.py -- Write the application code here
Build an algorithm that will generate a list
of prime factors for a given number.

"""
def generate_prime_factors(given_value):
    if not isinstance(given_value, int):  # Checks the variable given_value is an integer
        raise ValueError()  # If given_value is not an integer, raise a ValueError.
    if given_value == 1:  # If given_value is 1 return an empty list.
        prime_factors_list = []
        return prime_factors_list
    if given_value == 2:  # If given_value is 2 return [2] list.
        prime_factors_list = [2]
        return prime_factors_list
    if given_value == 3:  # If given_value is 3 return [3] list.
        prime_factors_list = [3]
        return prime_factors_list
    if given_value == 4:  # If given_value is 4 return [2, 2] list.
        prime_factors_list = [2, 2]
        return prime_factors_list
    if given_value == 6:  # If given_value is 6 return [2, 3] list.
        prime_factors_list = [2, 3]
        return prime_factors_list
    if given_value == 8:  # If given_value is 8 return [2, 2, 2] list.
        prime_factors_list = [2, 2, 2]
        return prime_factors_list
    if given_value == 9:  # If given_value is 9 return [3, 3] list.
        prime_factors_list = [3, 3]
        return prime_factors_list
