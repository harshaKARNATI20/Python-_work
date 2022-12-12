from functools import reduce

list1 = [3,2,8,16,11,34,17]
output1 = list(map(lambda i: i+2,list1))
output2 = reduce(lambda a,b: a+b,list1)
print(output2)

output3 = reduce(lambda a,b: a**2+b**2,list1)
print(output3)
output4 = reduce(lambda a,b: a*b,list1)
print(output4)