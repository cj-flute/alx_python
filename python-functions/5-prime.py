#!/usr/bin/python3
def is_prime(num):
    if num == 1 or num == 2 or num == 3:
        return True
    if num % 2 != 0 and num % 3 != 0:
        return False
    else:
        return True
    pass


print(is_prime(35))
