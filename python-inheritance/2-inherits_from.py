#!/usr/bin/python3

def inherits_from(obj, a_class):
    if issubclass(obj, a_class):
        return True
    else:
        return False


a = True
if inherits_from(type(a), int):
    print("{} inherited from class {}".format(a, int.__name__))
if inherits_from(type(a), bool):
    print("{} inherited from class {}".format(a, bool.__name__))
if inherits_from(type(a), object):
    print("{} inherited from class {}".format(a, object.__name__))
