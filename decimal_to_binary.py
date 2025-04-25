from math import ceil, log2

def convert_to_binary(n): # Transforms a dicimal number into a binary
    # Edge cases:
    if n == 0:
        return [0]
    if n == 1:
        return [1]

    bit_length = ceil(log2(n+1)) # Bit length equation
    binary = [1] + (bit_length-1)*[0]

    if n == 1 << (bit_length-1): # since all power of 2 are in the bit form 1...0*(bit_length - 1) we can simply take 1 and move bit length times making it instantaneous with a complexity of O(1)
        return binary

    for i in range(0, len(binary)): # Checks whether N is smaller than the next base (eg. ...,32,16,8,4,2,1), if so it will change binary[i] to 1 and N = N - column until N = 0
        column = 1 << (bit_length-1 - i)
        if column <= n:
            binary[i] = 1
            n -= column
        if n == 0:
            break

    return binary

print(1 << 4) 
print(convert_to_binary(16))