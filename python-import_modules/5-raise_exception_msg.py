#!/usr/bin/python3
def raise_exception_msg(value=""):
    try:
        print(value)
    except NameError as ne:
        print(ne)
    pass


def main():
    raise_exception_msg()
    pass


if __name__ == "__main__":
    main()
    pass
