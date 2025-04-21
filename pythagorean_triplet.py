from largestPrimeFactor import is_prime
import time
def pythagorean_triple():
    for i in range(2, 50):
        for j in range(1, i):
            a = i**2 - j**2
            b = 2 * i * j
            c = i**2 + j**2
            print(f"Testing i={i}, j={j} -> a={a}, b={b}, c={c}, sum={a + b + c}")
            if a + b + c == 1000:
                return f"Found: a={a}, b={b}, c={c}, product={a*b*c}"
start = time.time()
print(pythagorean_triple())
end = time.time()
print()
print(end - start)