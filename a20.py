# find large in 5 numbers
a = int(input('Enter A : '))
b = int(input('Enter B : '))
c = int(input('Enter C : '))
d = int(input('Enter D : '))
e = int(input('Enter E : '))

if a > b and a > c and a > d and a > e:
    print(f'{a} is largest')
elif b > c and b > d and b > e:
    print(f'{b} is largest')    
elif c > d and c > e:
    print(f'{c} is largest')
elif d > e:
    print(f'{d} is largest')        
else:
    print(f'{e} is largest')    