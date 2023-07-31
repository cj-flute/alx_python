#!/usr/bin/python3
def is_prime(num):
    if num == 1 or num == 2 or num == 3:
        return True
    if num < 0:
        return False
    if (num % 2 != 0 and num % 3 != 0
            and num % 5 != 0 and num % 7 != 0) or (num == 0):
        return True
    else:
        return False
    pass


def main():
    number = int(input())
    print(is_prime(number))
    pass


if __name__ == "__main__":
    main()
