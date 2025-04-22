from math import prod, gcd
def pgcd(*numbers : int):
    """
    this function will first take the square root of the smallest number to generate a Sieve
    of Eratosthenes, then find its factors and use them to check whether they are also factors of the remaining numbers and whether they hold the same count.
    Finally, it returns t he PGCD by finding the minimum of all potential products of factors from each number.

    Args:
        numbers (int): The numbers to find their PGCD
    
    Returns:
        int: The PGCD
    """
    # Edge case 1:
    if not numbers:
        raise ValueError("At least one number must be provided.")
    unique_numbers = list(set(numbers))
    if unique_numbers:
        # Creating the Sieve of Eratosthenes:
        min_number = min(unique_numbers)
        # Edge case 2:
        if min_number == 0:
            return 0
        # Edge case 3:
        if min_number == 1:
            return 1
        
        unique_numbers.remove(min_number)
        sieve_limit = int(min_number**.5)
        sieve = [True] * (sieve_limit + 1)
        sieve[0] = sieve[1] = False
        for p in range(2, int(sieve_limit**.5 + 1)):
            if sieve[p]:
                sieve[p*p : sieve_limit+1 : p] = [False] * len(sieve[p*p : sieve_limit+1 : p])
        prime_numbers = [p for p, is_prime in enumerate(sieve) if is_prime]

        
        # Finding the factors of the smallest number:
        factors = {}
        temp = min_number
        for prime in prime_numbers:
            exponent = 0
            while temp != 1 and not temp % prime:
                exponent += 1
                temp //= prime
            if exponent:
                factors[prime] = exponent
        # Edge case 4:
        if not factors:
            return 1

        # Checking the number of factors
        potential_pgcd = []
        new_factors = {}
        common_state = False
        for num in unique_numbers:
            temp = num
            for prime in factors:
                exponent = 0
                while not temp % prime and temp > 1:
                    exponent += 1
                    temp //= prime
                if exponent and exponent < factors[prime]:
                    common_state = True
                    factors[prime] = exponent
        pgcd = 1
        if common_state:
            for prime in factors:
                pgcd *= prime**factors[prime]

        return pgcd
    else:
        return numbers[0]

print(pgcd(456789, 98976, 99928,9390))
print(gcd(456789, 98976, 99928,9390))