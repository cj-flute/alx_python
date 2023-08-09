#!/usr/bin/python3
'''
    models module
    Holds class Base and Rectangle
    Rectangle class inherits from base class
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
            self._id = id
        else:
            Base.__nb_objects += 1
            self._id = Base.__nb_objects


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
        if type(width) == int:
            self.__width = width
        elif int(width) < 0:
            raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

        if type(height) == int:
            self.__height = height
        elif int(height) < 0:
            raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

        if type(x) == int:
            self.__x = x
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            raise TypeError("x must be an integer")

        if type(y) == int:
            self.__y = y
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            raise TypeError("y must be an integer")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if isinstance(width, int) and width > 0:
            self.__ = width
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            raise TypeError("Width must be an integer")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if isinstance(height, int) and height > 0:
            self.__ = height
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            raise TypeError("height must be an integer")

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if isinstance(x, int) and int(x) >= 0:
            self.__x = x
        elif int(x) <= 0:
            raise ValueError("x must be > 0")
        else:
            raise TypeError("x must be an integer")

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if isinstance(y, int) and int(y) >= 0:
            self.__y = y
        elif int(y) <= 0:
            raise ValueError("y must be > 0")
        else:
            raise TypeError("y must be an integer")

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, new_id):
        if isinstance(new_id, int):
            self._id = new_id
        else:
            raise ValueError("id must be an integer")

    def area(self):
        '''The area method '''
        return self.__width * self.__height


# try:
#     Rectangle(10, "2")
#     Rectangle.height
# except Exception as e:
#     print("[{}] {}".format(e.__class__.__name__, e))

# try:
#     r = Rectangle(10, 2)
#     r.width = -10
# except Exception as e:
#     print("[{}] {}".format(e.__class__.__name__, e))

# try:
#     r = Rectangle(10, 2)
#     r.x = {}
# except Exception as e:
#     print("[{}] {}".format(e.__class__.__name__, e))

# try:
#     Rectangle(10, 2, 3, -1)
# except Exception as e:
#     print("[{}] {}".format(e.__class__.__name__, e))
