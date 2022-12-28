# f = open("Harsha.jpg", "rb")



# f1 = open("img_copy.jpg","wb")

# # print(f.read())
# for i in f:
#     f1.write(i)

import os

if os.path.exists("demo1.txt"):
    os.remove("demo1.txt")
else:
    print("File does not exist")
