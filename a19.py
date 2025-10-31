# find large in 3 numbers
a = int(input('Enter A : '))
b = int(input('Enter B : '))
c = int(input('Enter C : '))

if a > b and a > c:
    print(f'{a} is largest')
elif b > c:
    print(f'{b} is largest')    
else:
    print(f'{c} is largest')    