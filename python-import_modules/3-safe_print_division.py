#!/usr/bin/python3
def safe_print_division(a, b):
    return a/b
    pass


a = 12
b = 2
try:
    result = safe_print_division(a, b)
    print("{:d} / {:d} = {}".format(a, b, result))
    pass
except ZeroDivisionError:
    result = "None"
    print("{:d} / {:d} = None".format(a, b))
    pass
finally:
    print("Inside result: {}".format(result))
    pass

a = 12
b = 0
try:
    result = safe_print_division(a, b)
    print("{:d} / {:d} = {}".format(a, b, result))
    pass
except ZeroDivisionError:
    result = "None"
    print("{:d} / {:d} = None".format(a, b))
    pass
finally:
    print("Inside result: {}".format(result))
    pass
