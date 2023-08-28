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
            raise ValueError("{}name must be greater than 0".format(self.name))
