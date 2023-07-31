#!/usr/bin/python3

def no_c(my_string):
    list_string = list(my_string)
    striped = [char for char in list_string if char not in ['c', 'C']]
    new_string = ''.join(striped)
    return new_string
    pass


def main():
    try:
        a_string = str(input())
        print(no_c(a_string))
    except TypeError:
        print("Not a string")
    pass


if __name__ == "__main__":
    main()
