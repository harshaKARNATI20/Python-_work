
# import sys
# sys.setrecursionlimit(2000)

# def hello():
#     print("Hello World")
#     hello()

# hello()


def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)




num = fact(100)
print(num)