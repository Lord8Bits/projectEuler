from math import ceil, log2
def exponentiation(n, exponent): # Divide and Conquer Method
    if exponent == 0:
        return 1
    if exponent == 1:
        return n
    if not exponent % 2:
        return exponentiation(n**2, exponent//2)
    if exponent > 2:
        return n * exponentiation(n**2, (exponent-1)//2)
    

def convert_to_binary(n): # Transforms a dicimal number into a binary
    
    if n == 0:
        return [0]
    if n == 1:
        return [1]
    
    bit_length = ceil(log2(n+1)) # Bit length equation
    binary = [1] + (bit_length-1)*[0]

    if n == exponentiation(2,bit_length-1): # if N equal to 2**(bit_length) it means the number is in the bit form 1...0*(bit_length - 1)
        return binary
    
    
    for i in range(0, len(binary)): 
        column = exponentiation(2, bit_length-1 - i)
        if column <= n:
            binary[i] = 1
            n -= column

        if n == 0:
            break
    return binary
print(convert_to_binary(3))