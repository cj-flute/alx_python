#!/usr/bin/python3
'''
    models module
    Holds class Base
'''


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
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


class Rectangle(Base):
    '''
        class Rectangle that inherits
        from the class Base
        attribute: width, height, x, y and id
        each attributes have a getter and setter
        def __init__(self, width, height, x=0, y=0, id=None)
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''
            Rectangle.__init__()
            def __init__(self, width, height, x=0, y=0, id=None)
        '''
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width
        return self.__width

    @property
    def height(self):
        return self.__height

    @height.setter
    def width(self, height):
        self.__height
        return self.__height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x
        return self.__x

    @property
    def y(self):
        return self.__y

    @y.setter
    def width(self, width):
        self.__y
        return self.__y
