user = input("Enter the word :")

if user[-1]=="e":
    a=list(user)
    a.remove("e")
    print(str(a)+"ing")
elif len(user) > 3:
    print(user +"ing")
else:
    print(user)







