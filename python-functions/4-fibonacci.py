#!/urs/bin/python3
def fina(x):
    if x == 1:
        return 1
    elif x == 0:
        return 0
    elif x > 1:
        return fina(x - 1) + fina(x - 2)


def fibonacci_sequence(t):
    lis = []
    for i in range(t):
        lis.append(fina(i))
    return lis


def main():
    num = int(input())
    print(fibonacci_sequence(num))
    pass


if __name__ == "__main__":
    main()
