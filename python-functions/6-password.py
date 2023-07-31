#!/usr/bin/python3
password = input()

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


def pass_validator(pword):
    if len(password) > 8:
        if (upper(password) and
                lower(password) and
                nums(password)):
            return True
        else:
            False
    else:
        return False


def main():
    print(pass_validator(password))
    pass


if __name__ == "__main__":
    main()
