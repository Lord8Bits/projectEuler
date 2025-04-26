from math import ceil, log2

def convert_to_binary(n):  # Transforms a decimal number into a binary
    # Edge cases:
    if n == 0:
        return [0]
    if n == 1:
        return [1]
    
    bit_length = ceil(log2(n+1))  # Bit length equation
    binary = [0] * bit_length  # Create a binary list filled with 0s

    powers_of_2 = [1 << i for i in range(bit_length-1,-1,-1)]  # List of powers of 2 up to bit_length-1

    for i, column in enumerate(powers_of_2):  # Iterate through the powers of 2
        if n >= column:  # Check if the number is greater than or equal to the current power of 2
            binary[i] = 1
            n -= column  # Subtract the power of 2 from the number

    return binary

print(1 << 4)
print(convert_to_binary(16))