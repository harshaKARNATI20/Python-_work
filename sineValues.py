# Take Two integers a and b
# Print all the sine values of all the integers in the given range of a and b
import math
a = int(input())
b = int(input())
for i in range(a,b+1):
    print(f'{math.sin(i):.2f}')



