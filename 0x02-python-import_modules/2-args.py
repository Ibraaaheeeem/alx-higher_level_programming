#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    l = len(sys.argv) - 1
    if l == 0:
        print("{:d} arguments.".format(l))
    elif l == 1:
        print("{:d} argument:".format(l))
    else:
        print("{:d} arguments:".format(l))
    for i in range(1, len(sys.argv)):
        print("{:d}: {:s}".format(i, sys.argv[i]))

