sum_square = sum(x**2 for x in range(1,101))
square_ofSum = sum(x for x in range(1,101))**2
print(square_ofSum - sum_square)