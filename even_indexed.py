def even_ind(str1):
    a=''
    for i in range(len(str1)):
        if i%2==0:
            a+=str1[i]

    return a
n=input()
print(even_ind(n))