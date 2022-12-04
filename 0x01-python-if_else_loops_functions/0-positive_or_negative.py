#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number == 0:
    print("{:d} is zero\n")
elif number > 0:
    print("{:d} is positive\n")
else:
    print("{:d} is negative\n") 
