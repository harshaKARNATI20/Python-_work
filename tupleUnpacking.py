# tuple1 = ("car","bike","boat")
# (item1,item2,item3) = tuple1

# print(item1)
# print(item2)
# print(item3)

tuple1 = ("car","bike","boat","cycle")
(item1,*item2,) = tuple1

print(item1)
print(item2)

# '*' represents astrick that can take 'n' no. of values

