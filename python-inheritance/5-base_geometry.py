#!/urs/bin/python3

'''3-base_geometry.py'''


class BaseGeometry:
    '''
        BaseGeometry class      
    '''

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
