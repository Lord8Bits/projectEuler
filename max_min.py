x = int(input())
y = int(input())
z = int(input())

if x > y > z:
    print(x, ' is maximum')
    print(z, ' is minimum')
elif x > z > y:
    print(x, ' is maximum')
    print(y, ' is minimum')
elif y > x > z:
    print(y, ' is maximum')
    print(z, ' is minimum')
elif y > z > x:
    print(y, ' is maximum')
    print(x, ' is minimum')
elif z > x > y:
    print(z, ' is maximum')
    print(y, ' is minimum')
else:
    print(z, ' is maximum')
    print(x, ' is minimum')

