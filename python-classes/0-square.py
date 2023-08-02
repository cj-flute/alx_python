#!/usr/bin/python3
'''
python3 -c 'print(__import__("my_module").__doc__)'
'''


class Square:
    '''
    python3 -c 'print(__import__("my_module").MyClass.__doc__)'
    '''

    def __init__(self, size):
        '''
        python3 -c 'print(__import__("my_module").my_function.__doc__)' and 
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        '''
        self.__size = size


my_sqaure = Square(3)
print(type(my_sqaure))
print(my_sqaure.__dict__)

# try:
#     print(my_sqaure.size)
# except Exception as e:
#     print(e)

# try:
#     print(my_sqaure.__size)
# except Exception as e:
#     print(e)
