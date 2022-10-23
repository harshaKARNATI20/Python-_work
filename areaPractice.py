a = int(input("Enter Side 1 :"))
b = int(input("Enter Side 2 :"))
c = int(input("Enter Side 3 :"))
s = (a + b + c)/2
area = (s*(s-a)*(s-b)*(s-c))**0.5

print("The area is : %0.2f"%area)


