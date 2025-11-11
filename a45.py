# 1. List
#           0     1       2        3     4         5
colors = ['red','green','white','pink','yellow','orange'] # list
nums = [23,78,90,32,45,60] # list

# 1. Access or print a list
print(colors)
print(nums)
# 2. Access or print a single data
print(colors[4])
print(nums[2])
sum = nums[1] + nums[5]
print(sum)
# 3. Slicing of data in a list
print(colors[1:4])
print(nums[2:4])
# 4. access a list using for loop
for c in colors:
    print(c,end=' ')