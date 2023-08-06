#!/usr/bin/python3
from base import Base
'''
    Rectangle class inherits from base class
'''


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
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y
