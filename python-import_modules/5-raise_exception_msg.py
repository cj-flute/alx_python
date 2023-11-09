#!/usr/bin/python3
def raise_exception_msg(message=""):
    class CustomException(Exception):
        def __init__(self, message):
            self.message = message
            super().__init__(self.message)

    raise CustomException(message)


if __name__ == "__main__":
    try:
        raise_exception_msg("C is fun")
    except NameError as ne:
        print(ne)
