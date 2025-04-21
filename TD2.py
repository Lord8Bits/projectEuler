

def suite_recursive(n):
    if n < 2:
        return 1
    else:
        return 3*suite_recursive(n - 1)+suite_recursive(n - 2)

def max_two(x,y):
    if x < y:
        return y
    else:
        return x
def max_three(x,y,z):
    return max_two(z, max_two(x,y))

def max_four(x,y,z,f):
    return max_two(f, max_three(x,y,z))


