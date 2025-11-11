# 1. List
#  Functions in List - len(), min(), max(), type(), tuple()

colors = ['red','green','white','pink','yellow','orange','grey','magenta','blue'] # list
nums = [23,78,90,32,45,60,34,67,91,11] # list

print(len(colors))
print(len(nums))

print(min(colors))  # green
print(min(nums)) # 23

print(max(colors)) # yellow
print(max(nums)) # 91

print(type(colors)) # class<'list'>
print(type(nums)) # class<'list'>

t1 = tuple(colors) # convert a list into tuple
print(t1)
print(type(t1)) # class<'tuple'>