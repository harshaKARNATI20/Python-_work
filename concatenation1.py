name = input("Enter your name")

if len(name)%2==0:
    print("Middle charc is :",name[(len(name)+1)//2])
else:
    print("Middle charc is :",name[(len(name))//2])


