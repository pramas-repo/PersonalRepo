# another example of i/o function
rno = int(input('Enter Rno : '))
name = input('Enter Name : ')
ph = int(input('Enter Phy marks : '))
ch = int(input('Enter Che marks : '))
ma = int(input('Enter Maths marks : '))

gt = ph + ch + ma
per = gt / 3.0
print(f'Rno = {rno} Name = {name} Gt = {gt} Per = {round(per,2)}')