#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
new_number = str(number)

if number > 0 and int(new_number[-1]) != 0:
    if int(new_number[-1]) > 5:
        print("Last digit of {0} is {1} and is greater than 5".format(number, new_number[-1]))
    else:
        print("Last digit of {0} is {1} and is less than 6 and not 0".format(number, new_number[-1]))
elif (number < 0 and int(new_number[-1]) == 0) or (number > 0 and int(new_number[-1]) == 0) :
        print("Last digit of {0} is {1} and is 0".format(number, new_number[-1]))
else:
    print("Last digit of {0} is -{1} and is less than 6 and not 0".format(number, new_number[-1]))
