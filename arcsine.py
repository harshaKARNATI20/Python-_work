import math
a=float(input())
if -1<=a<=1:
    b=math.atan(a)
    print(f'{b :.4f}')
else:
    print("invalid")
    