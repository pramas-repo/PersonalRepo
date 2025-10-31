# generate multiplication table of a number using while loop
n = int(input('Enter a number : '))

i = 1
while i <=10:
    k = n * i
    print(f'{n} x {i} = {k}') # 5 x 3 = 15
    i+=1


