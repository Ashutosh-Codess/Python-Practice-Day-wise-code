#Prime Range Analyzer
from math import isqrt

def is_prime(n: int) -> bool:
    if n < 2:
        return False

    if n % 2 == 0:
        return n == 2
    
    for i in range(3, isqrt(n) + 1, 2):
        if n % i == 0:
            return False
    return True

def count_primes(A: int, B: int) -> int:
    return sum(is_prime(x) for x in range(A, B + 1))