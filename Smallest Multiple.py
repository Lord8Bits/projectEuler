from math import gcd
def lcm(a, b):
    return a * b // gcd(a, b)

# Calculate the LCM of numbers from 1 to 20
result = 1
for i in range(1, 21):
    result = lcm(result, i)

print(result)

n = 20
modulo = [2**4, 3**2, 5, 7, 11, 13, 17, 19]
while sum(n % d for d in modulo) != 0:
    n+= 20


print(n)