#!/usr/bin/python3
def safe_print_division(a, b):
    return a/b
    pass


def main():
    a = int(input())
    b = int(input())
    try:
        result = safe_print_division(a, b)
        pass
    except ZeroDivisionError:
        result = "None"
        pass
    finally:
        print("Inside result: {}".format(result))
        print("{:d} / {:d} = {}".format(a, b, result))
        pass


if __name__ == "__main__":
    main()
