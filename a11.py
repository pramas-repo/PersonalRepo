# print() with format() function
ht = 5
ba = 3

areat = 0.5 * ht * ba

# Unindexed place holder {}
print('Ht = {} Base = {} Area of Triangle = {}'.format(ht,ba,areat))
# padding of data in place holder - by default numeric data right aligned
print('Ht = {:10} Base = {:10} Area of Triangle = {:10}'.format(ht,ba,areat))
# changing the data lign can be done by < - left, > - right, ^ - center align
print('Ht = {:<10} Base = {:<10} Area of Triangle = {:<10}'.format(ht,ba,areat))
print('Ht = {:>10} Base = {:>10} Area of Triangle = {:>10}'.format(ht,ba,areat))
print('Ht = {:^10} Base = {:^10} Area of Triangle = {:^10}'.format(ht,ba,areat))
# replacing blank spaces with some special character, generally *
print('Ht = {:*<10} Base = {:*<10} Area of Triangle = {:*<10}'.format(ht,ba,areat))
print('Ht = {:*>10} Base = {:*>10} Area of Triangle = {:*>10}'.format(ht,ba,areat))
print('Ht = {:*^10} Base = {:*^10} Area of Triangle = {:*^10}'.format(ht,ba,areat))