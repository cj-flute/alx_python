#!/urs/bin/python3
def f(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    elif n > 1:
        return f(n - 1) + f(n - 2)
    pass
