#!/usr/bin/python3
import random
import math
number = random.randint(-10000, 10000)
rem = math.floor(math.fmod(number, 10))
base = "Last digit of "+str(number) + " is " + str(rem)
if rem > 5:
    print(f"{base} and is greater than 5")
elif rem == 0:
    print(f"{base} and is 0")
elif rem < 6:
    print(f"{base} and is less than 6 and not 0")
