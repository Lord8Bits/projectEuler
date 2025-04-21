import time
from math import floor
from math import sqrt

def is_prime(n):
    if n <= 1:
        return False

    if n <= 3:
        return True

    if not n % 2 or not n % 3:
        return False

    limit = floor(sqrt(n))
    for i in range(5, limit + 1, 6):
        if not n % i or not n % (i + 2):
            return False
    return True

def sum_primes():
    result = 0
    for i in range(2000000):
        if is_prime(i):
            result += i
    return result

start = time.time()
print(sum_primes())
end = time.time()
print()
print(end - start)