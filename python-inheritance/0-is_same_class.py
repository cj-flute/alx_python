#!/usr/bin/python3
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
    if isinstance(obj, a_class):
        return True
    elif isinstance(obj, int):
        return "{} is an instance of the class int".format(obj)
    else:
        return False
