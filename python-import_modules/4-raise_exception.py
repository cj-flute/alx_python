#!/usr/bin/python3
def raise_exception():
    value = "Hello"
    try:
        value += 10
    except TypeError:
        print("Exception has been raised")
    pass


def main():
    raise_exception()
    pass


if __name__ == "__main__":
    main()
    pass
