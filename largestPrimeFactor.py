from math import sqrt
from math import floor
import time

def is_prime(n):
    if n <= 1:
        return False

    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    limit = floor(sqrt(n))
    for i in range(5, limit + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def find_largest_prime_factor(n):
    for i in range(int(n ** 0.5), 1, -1):
        if n % i == 0:
            if is_prime(i):
                counterpart = n // i
                if is_prime(counterpart):
                    return counterpart
                return i
    return None

print(find_largest_prime_factor(5678039817))