def find_palindrome():
    max_product = 0
    max_i = 0
    max_j = 0
    for i in range(110, 1000, 11):
        for j in range(i, 1000):
            product = str(i*j)
            if product == product[::-1] and int(product) > max_product:
                    max_product = int(product)
                    max_i, max_j = i, j
    return max_product, max_i, max_j

print(find_palindrome())