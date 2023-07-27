#!/usr/bin/python3
from add_0 import *

a = 1
b = 2


def main():
    added = add(a, b)
    print("{0} + {1} = {2}".format(a, b, add(a, b)), end="\n")
    pass


if __name__ == "__main__":
    main()
