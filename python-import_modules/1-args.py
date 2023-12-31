# 1/usr/bin/python3
import sys


def out_arguments(argv):
    number_of_arguments = len(argv) - 1
    plural = "s" if number_of_arguments != 1 and number_of_arguments != 0 else ""
    if number_of_arguments == 0:
        print(f"{number_of_arguments} arguments.", end="\n")
    else:
        print(f"{number_of_arguments} argument{plural}:", end="")
    if number_of_arguments > 0:
        print()
        for i, arg in enumerate(argv[1:], start=1):
            print(f"{i}: {arg}")


if __name__ == "__main__":
    out_arguments(sys.argv)
