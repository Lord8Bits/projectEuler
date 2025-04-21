
import random
import time

def is_prime(n):
    """Check for primality using a combination of trial division."""
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def pollards_rho(n):
    """Pollard's rho algorithm for finding a non-trivial factor of n."""
    if n % 2 == 0:
        return 2
    x = random.randint(2, n - 1)
    y = x
    c = random.randint(1, n - 1)
    d = 1

    while d == 1:
        x = (x * x + c) % n
        y = (y * y + c) % n
        y = (y * y + c) % n
        d = gcd(abs(x - y), n)
        if d == n:
            return pollards_rho(n)
    return d

def gcd(a, b):
    """Calculate the greatest common divisor using Euclid's algorithm."""
    while b:
        a, b = b, a % b
    return a

def find_largest_prime_factor(n):
    """Find the largest prime factor of n using Pollard's rho algorithm for factorization."""
    largest_prime = None
    # Loop until the number is fully factorized
    while n > 1:
        if is_prime(n):
            largest_prime = n
            break
        # Get a factor using Pollard's rho
        factor = pollards_rho(n)
        # Divide out all occurrences of this factor
        while n % factor == 0:
            n //= factor
        # Update the largest prime if this factor is prime
        if is_prime(factor):
            largest_prime = factor
    return largest_prime


start_time = time.time()

print(find_largest_prime_factor(7474748128468694195))

end_time = time.time()
execution_time = end_time - start_time
print(execution_time)