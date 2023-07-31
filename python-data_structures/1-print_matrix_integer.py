#!/usr/bin/python3
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][0], matrix[i][1], matrix[i][2] = matrix[i]
            if j < 2:
                print("{:d}".format(matrix[i][j]), end=" ")
            elif j == 2:
                print("{:d}".format(matrix[i][j]), end="")
        print(end="\n")
    pass


def main():
    print_matrix_integer(matrix)
    print("--", end="\n")
    print_matrix_integer()
    pass


if __name__ == "__main__":
    main()
