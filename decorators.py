def div(a,b):
    print(a/b)

def new_div(func):

    def innerFunc(a,b):
        if a < b:
            a,b = b,a
        return func(a,b)

    return innerFunc
div = new_div(div)
div(3,66)




# when you can't change the original function,apply decorators as above
# 1 in other is called nested 
