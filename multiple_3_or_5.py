def multiple_3or5(max_number):
    multiples = []
    for i in range(max_number):
        if i % 5 == 0 or i % 3 == 0:
            multiples.append(i)

    print(sum(multiples))

multiple_3or5(1000)