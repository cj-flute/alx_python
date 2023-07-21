#!/urs/bin/python3
def fina(x):
    if x == 1:
        return 1
    elif x == 0:
        return 0
    elif x > 1:
        return fina(x - 1) + fina(x - 2)


def fx(t):
    lis = []
    for i in range(t):
        lis.append(fina(i))
    return lis


print(fx(10))
