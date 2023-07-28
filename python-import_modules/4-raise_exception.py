#!/usr/bin/python3
def raise_exception():
    value = "Hello"
    try:
        value += 10
    except TypeError:
        print("Exception has been raised")


raise_exception()
