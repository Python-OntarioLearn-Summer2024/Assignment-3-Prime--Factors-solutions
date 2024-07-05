"""
prime.py -- Write the application code here
"""
def generate_prime_factors(n):
    prime = []
    divisor = 2
    while divisor <=n:
        if n% divisor == 0:
            prime.append(divisor)
        else:
            divisor +=1
    return  prime
