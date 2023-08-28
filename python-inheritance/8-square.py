#!/urs/bin/python3

'''3-base_geometry.py'''


class BaseGeometry:
    '''
        BaseGeometry class      
    '''

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.name = name
        self.value = value

        if type(self.value) != int:
            raise TypeError("{} must be an integer".format(self.name))
        elif self.value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))


class Rectangle(BaseGeometry):
    '''
        Rectangle class that inherits from BaseGeometry class
    '''

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        w = self.__width
        h = self.__height

        if type(w) != int:
            raise TypeError("width must be an integer")
        elif w <= 0:
            raise ValueError("width must be greater than 0")

        if type(h) != int:
            raise TypeError("height must be an integer")
        elif h <= 0:
            raise ValueError("height must be greater than 0")

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[{0}] {1}/{2}".format(__class__.__name__, self.__width,
                                      self.__height)


class Square(Rectangle):
    def __init__(self, size):
        self.__size = size
        s = self.__size

        if type(s) != int:
            raise TypeError("size must be an integer")
        elif s <= 0:
            raise ValueError("size must be greater than 0")

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return "[{0}] {1}/{2}".format(Rectangle.__name__, self.__size, self.__size)
