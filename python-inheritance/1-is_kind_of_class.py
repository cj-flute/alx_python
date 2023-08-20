#!/usr/bin/python3
'''
    Exact same pbject
    A function is_kind_of_class(obj, a_class) that check if the object is an instance of 
    a class
'''


def is_kind_of_class(obj, a_class):
    '''
        is_kind_of_class(obj, a_class):
            if isinstance(obj, a_class):
            return True
        else:
            return False
    '''
    if isinstance(obj, a_class):
        return True
    else:
        return False
