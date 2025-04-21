import time


def lcs():
    max_n = 0
    max_cnt = 0
    lcs_cache = {}  # Cache that stores previously calculated value. this process is called memoization
    for n in range(1, 1000000):
        cnt = 0
        temp_n = n  # temporary n variable to not overwrite
        while temp_n != 1:
            if temp_n in lcs_cache:
                cnt += lcs_cache[temp_n]  # directly adds the chain size of the number in cache
                break
            if not temp_n % 2:
                temp_n //= 2
                cnt += 1
            else:
                temp_n = 3 * temp_n + 1
                cnt += 1

        if cnt > max_cnt:
            max_cnt = cnt
            max_n = n
        lcs_cache[n] = cnt  # adds a new calculated n to reduce runtime
    return f'The longest Collatz sequence under 1mil is: {max_n} with a chain count of {max_cnt}'
start = time.time()
print(lcs())
end = time.time()
print()
print(end - start)