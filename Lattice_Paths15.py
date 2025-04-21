from math import factorial
def hm_paths_in_grid(size):
    return factorial(size*2) // (factorial(size)**2)
print(hm_paths_in_grid(20))
