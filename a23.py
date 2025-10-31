# another example of a while loop
# sum of 1 to n numbers
n = int(input('Enter a number : ')) # n = 10

sum = 0
i = 1

while i<=n: # 10
    sum = sum + i
    i+=1
    
print(f'Sum of 1 to {n} numbers = {sum}')    