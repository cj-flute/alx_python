#!/usr/bin/python3
def safe_print_division(a, b):
    return a/b
    pass


def main():
    a = int(input())
    b = int(input())
    try:
        result = safe_print_division(a, b)
        print("Inside result: {}".format(result))
        pass
    except ZeroDivisionError:
        result = "None"
        print("Inside result: {}".format(result))
        pass
    finally:
        print("{:d} / {:d} = {}".format(a, b, result))
        pass

    pass


if __name__ == "__main__":
    main()
