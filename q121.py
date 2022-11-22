# Take three numbers from the user and 
# Find the GCD of the three numbers without using any operators
import math
a = int(input())
b = int(input())
c = int(input())
print(math.gcd(math.gcd(a,b),c))

