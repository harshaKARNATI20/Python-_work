def digit(x):
    a=len(x)
    p="1"
    for i in range (a-1):
        p+="0"
    s=int(x)/int(p)

    return s
x=input()
print(format(digit(x),".2f"))






