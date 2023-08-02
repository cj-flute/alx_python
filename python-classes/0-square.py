#!/usr/bin/python3
class Square:
    def __init__(self, size):
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
