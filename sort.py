def slicing(str,ind):
    a=""
    if len(str)>ind+1:
        for i in range(ind+2):
            a+=str[i]
    else:
        print("Index out of range")
    print(a)
a=input()
i=int(input())
slicing(a,i)