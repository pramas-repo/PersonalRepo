# 1. print() function in Python
rad = 13
areac = 3.14 * (rad * rad)

# 1. Concatanation method with + symbol and str()
print('Radius = ' + str(rad) + ' Area of Circle = ' + str(areac))
# 2. comma as a data separator method
print('Radius = ',rad,' Area of Circle = ',areac)
# 3. formatted string method
print(f'Radius = {rad} Area of Circle = {areac}') # {} are called place holders
# 4. print() with format() function
print('Radius = {} Area of Circle = {}'.format(rad,areac))
