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
            python3 -c 'print(__import__("0-square").__init__.__doc__)
            python3 -c 'print(__import__("0-square").Square.__init__.__doc__)
        '''
        self.__size = size
