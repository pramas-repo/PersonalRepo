# simple math calculator
a = int(input('Enter a number : '))
op = input('Enter Operator (+, -, *, /) : ')
b = int(input('Enter a number : '))

if op == '+':
    res = a + b
    print('Result = {}'.format(res))
elif op == '-':  
    res = a - b
    print('Result = {}'.format(res))
elif op == '*': 
    res = a * b
    print('Result = {}'.format(res))
elif op == '/': 
    res = a / b
    print('Result = {}'.format(res))
else:
    print("Not a math operator")