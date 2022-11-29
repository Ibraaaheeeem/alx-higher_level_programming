#!/usr/bin/python3
flag = True
stringZYX = ""
for i in range(ord("z"), ord("a")-1, -1):
    if flag:
        # print("{:c}".format(i), end="")
        stringZYX += chr(i)
    else:
        # print("{:c}".format((i-32), end=""))
        stringZYX += chr(i - 32)
    flag = not flag
print(stringZYX, end="")
