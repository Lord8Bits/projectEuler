import time

series = int('73167176531330624919225119674426574742355349194934'
            '96983520312774506326239578318016984801869478851843'
            '85861560789112949495459501737958331952853208805511'
            '12540698747158523863050715693290963295227443043557'
            '66896648950445244523161731856403098711121722383113'
            '62229893423380308135336276614282806444486645238749'
            '30358907296290491560440772390713810515859307960866'
            '70172427121883998797908792274921901699720888093776'
            '65727333001053367881220235421809751254540594752243'
            '52584907711670556013604839586446706324415722155397'
            '53697817977846174064955149290862569321978468622482'
            '83972241375657056057490261407972968652414535100474'
            '82166370484403199890008895243450658541227588666881'
            '16427171479924442928230863465674813919123162824586'
            '17866458359124566529476545682848912883142607690042'
            '24219022671055626321111109370544217506941658960408'
            '07198403850962455444362981230987879927244284909188'
            '84580156166097919133875499200524063689912560717606'
            '05886116467109405077541002256983155200055935729725'
            '71636269561882670428252483600823257530420752963450')
def largest_product_num(n):
    new_num = [] #This variable will serve as our a list for separating digits from 0s
    i = 0 #For index cuz why not
    save = '' #To save the digits except 0s
    string_n = str(n)

    #Uses 0s as stopping points and adds any other digit as a number in the 'new_num' list:
    while i < len(string_n):
        if string_n[i] == '0':
            if save != '' and len(save) >= 13:
                new_num.append(int(save))
            save = ''
        else:
            save += string_n[i]
        i += 1
    if save:
        new_num.append(int(save))

    #Finally it multiplies each 13 digits and adds it to product list to find the biggest product later
    product_list = []
    for number in new_num:
        #Starts by doing the easy part of length 13 numbers
        string_number = str(number)

        if len(string_number) == 13:
            prod = 1
            for digit in string_number:
                prod *= int(digit)
            product_list.append(prod)

        #The harder part:
        elif len(string_number) > 13:
            for i in range(len(string_number)): #It will start by indexing the str number
                prod = 1
                for digit in string_number[i:i+13]: #It will multiply each 13 adjacent digits and add it to prod variable
                    prod *= int(digit)
                product_list.append(prod) #Adds prod and prod2 to the product list

    return max(product_list) if product_list else 0 #Returns the biggest product

start = time.time()
print(largest_product_num(series))
end = time.time()
print()
print(end - start)


