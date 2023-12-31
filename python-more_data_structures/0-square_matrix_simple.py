#!/usr/bin/python3
def square_matrix_simple(matrix=None):
    new_matrix = [[x * x for x in r] for r in matrix]
    return new_matrix


def main():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    new_matrix = square_matrix_simple(matrix)
    print(new_matrix)
    print(matrix)


if __name__ == "__main__":
    main()
