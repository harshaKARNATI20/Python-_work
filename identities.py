import math
x=int(input())
y=int(input())
a=math.radians(x)
b=math.radians(y)
c=math.sin(a)*math.sin(b)-math.cos(a)*math.cos(b)
print(f'{c :.2f}')