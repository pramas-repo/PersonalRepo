# 1. Input/output functions in Python
# print() - output and input() - data entry function
# vol = 3.14  (rad * rad) * ht
rad = float(input('Enter Radius : '))
ht = float(input('Enter Height : '))

vol = 3.14 * (rad * rad) * ht
print(f'Radius = {rad} Height = {ht} Volume = {vol}')
