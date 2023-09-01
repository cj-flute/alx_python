#!/usr/bin/python3

# check for Uppercase in password


def upper(pword):
    upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    upper_letters_list = list(upper_letters)
    for i in range(len(pword)):
        if pword[i] not in upper_letters_list:
            continue
        else:
            return True
            break


# check for lowercase in password
def lower(pword):
    lower_letters = "abcdefghijklmnopqrstuvwxyz"
    lower_letters_list = list(lower_letters)
    for i in range(len(pword)):
        if pword[i] not in lower_letters_list:
            continue
        else:
            return True
            break

# check for space in password


def space(pword):
    if ' ' in pword:
        return True


# check for numbers in the password
def nums(pword):
    nums = "1234567890"
    nums_list = list(nums)
    for i in range(len(pword)):
        if pword[i] not in nums_list:
            continue
        else:
            return True
            break

# validator funtion


def validate_password(pword):
    if len(pword) > 8:
        if upper(pword):
            if lower(pword):
                if nums(pword):
                    if not space(pword):
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False
