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

        if w <= 0:
            raise ValueError("width must be greater than 0")
        elif type(w) != int:
            raise TypeError("width must be an integer")

        if h <= 0:
            raise ValueError("heigth must be greater than 0")
        elif type(h) != int:
            raise TypeError("heigth must be an integer")
