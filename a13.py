# input() function in python
# every data entered by input() function is string

name = input('Enter Your name : ')
age = int(input('Enter Your Age : '))

print('Name = {:s} Age = {:d}'.format(name,age))

print(type(name)) # type() function show data type of a variable
print(type(age))