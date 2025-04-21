from math import sqrt
def first_triangle_n(d):
    n_th = 1
    triangle_num = 1
    while True:
        n_div = 0
        limit = int(sqrt(triangle_num))
        for i in range(1, limit+1):
            if not triangle_num % i:
                if i * i == triangle_num:
                    n_div += 1  # i and (triangle_num // i) are the same, count only once
                else:
                    n_div += 2  # i and (triangle_num // i) are distinct, count both
        if limit**2 == triangle_num:
            n_div -= 1
        if n_div > d:
            return n_th*(n_th+1)//2

        n_th += 1
        triangle_num += n_th
print(first_triangle_n(500))
