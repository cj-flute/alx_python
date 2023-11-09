#!/usr/bin/python3
def safe_print_division(a=0, b=0):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
        print("{:d} / {:d} = {}".format(a, b, result))
        return result


def main():
    safe_print_division()


if __name__ == "__main__":
    main()
