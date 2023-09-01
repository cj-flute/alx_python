#!/usr/bin/python3
def is_prime(num):
    if type(num) == int:
        if (num == 2 or num == 3
                or num == 5 or num == 7 or
                num == 11):
            return True
        if num <= 0 or num == 1:
            return False
        if (num % 2 != 0 and num % 3 != 0
                or num % 5 != 0 and
                num % 7 != 0 and
                num % 11 != 0):
            return True
        else:
            return False
    else:
        return False
    pass
