base = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety', 'hundred', 'thousand']

sum_letters = 0
cache = {0: 0} #Cache for previously calculated words
i = 1 # This is to add the corresponding number to cache
for n in base[:19]: # Loop from 1 to 19
    sum_letters += len(n)
    cache[i] = len(n)
    i += 1
i = 20 # It will start in 20 and will get +10 each loop
for n in base[19:27]:
    l = len(n) #To reduce calculations
    for j in range(10):
        sum_letters += l + cache[j]
        cache[i+j] = l + cache[j] #This will add for example cache[20+1] = len('twenty') + cache[1], with cache[1] = len('one') from the first loop
    i += 10
hundred_length = len(base[27])
for i in range(1, 10):  # One hundred, two hundred, etc.
    for j in range(100):  # Numbers from 0 to 99
        if j == 0:
            sum_letters += hundred_length + cache[i]
        else:
            sum_letters += hundred_length + cache[i] + cache[j] + 3  # +3 is for the word 'and'

print(sum_letters+len(base[-1])+cache[1]) # it ends with the sum + len('one')+len('thousand')
