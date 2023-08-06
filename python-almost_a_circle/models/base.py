#!/usr/bin/python3
class Base:
    '''models/base
        Base class with private class attribute __nb_object = 0
        def __init__(self, id=None):
            if id != None:
                self.id = id
            else:
                Base.__nb_objects += 1
                self.id = Base.__nb_objects
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        '''
            Base.__init__()
            instance id
        '''
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
