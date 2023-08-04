#!/usr/bin/python3
'''
    python3 -c 'print(__import__("1-square").__doc__)
'''


class Square:
    '''
        python3 -c 'print(__import__("1-square").Square.__doc__)
    '''

    def __init__(self, size=0):
        '''
            python3 -c 'print(__import__("1-square").__init__.__doc__)
            python3 -c 'print(__import__("1-square").Square.__init__.__doc__)
        '''
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise TypeError("size must be >= 0")

    def area(self):
        '''
            python3 -c 'print(__import__("1-square").__init__.__doc__)
            python3 -c 'print(__import__("1-square").Square.area.__doc__)
        '''
        area = self.__size ** 2
        return area
