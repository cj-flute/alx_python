#!/usr/bin/python3
'''
python3 -c 'print(__import__("0-square").__doc__)'
'''


class Square:
    '''
    python3 -c 'print(__import__("0-square").Square.__doc__)'
    '''

    def __init__(self, size):
        '''
        python3 -c 'print(__import__("0-square").__init__.__doc__) 
        python3 -c 'print(__import__("0-square").Square.__init.__doc__)
        '''
        self.__size = size


my_sqaure = Square(3)
print(type(my_sqaure))
print(my_sqaure.__dict__)

try:
    print(my_sqaure.size)
except Exception as e:
    print(e)

try:
    print(my_sqaure.__size)
except Exception as e:
    print(e)
