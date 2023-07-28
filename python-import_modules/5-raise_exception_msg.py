#!/usr/bin/python3
def raise_exception_msg():
    try:
        print(value)
    except NameError:
        value = input()
        print(value)
    pass


def main():
    raise_exception_msg()
    pass


if __name__ == "__main__":
    main()
    pass
