def pds(power):
    return sum(int(digit) for digit in str(2**power))

print(pds(1000))