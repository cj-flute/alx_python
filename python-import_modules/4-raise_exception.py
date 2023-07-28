#!/usr/bin/python3
def raise_exception():
    value = "Hello"
    try:
        value += 10
    except TypeError as te:
        print("Exception raised")


raise_exception()
