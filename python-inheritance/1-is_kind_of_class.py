#!/usr/bin/python3
'''
    Exact same pbject
    Class A()
    A function is_same_class(obj, a_class) that check if the object is an instance of 
     a class
'''


class A:
    '''
        A class A()
    '''

    def __init__(self):
        '''
            A.__init__()
        '''
        pass


def is_same_class(obj, a_class):
    '''
        is_same_class(obj, a_class):
            if isinstance(obj, a_class):
                return True
            elif isinstance(obj, int):
                return "{} is an instance of the class int".format(obj)
            else:
                return False
    '''
    if isinstance(obj, a_class):
        if (type(obj) == bool or obj == None):
            return False
        return True
    elif isinstance(obj, int):
        return "{} is an instance of the class int".format(obj)
    elif isinstance(obj, list):
        return True
    else:
        return False


def is_kind_of_class(obj, a_class):
    '''
        is_kind_of_class(obj, a_class):
            if issubclass(obj, a_class):
            return True
        else:
            return False
    '''
    if issubclass(obj, a_class):
        return True
    else:
        return False
