from largestPrimeFactor import is_prime
import time

count = 0
prime = 1
while count < 100001:
    prime += 1
    if is_prime(prime):
        count += 1

start = time.time()
print(f'The 10001st prime number is: {prime}')
end = time.time()
print()
print(end - start)