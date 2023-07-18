#!/urs/bin/python3
for i in range(9):
    for e in range(10):
        if i == 1:
            e += 2
            if e > 9:
                continue
        elif i == 2:
            e += 3
            if e > 9:
                continue
        elif i == 3:
            e += 4
            if e > 9:
                continue
        elif i == 4:
            e += 5
            if e > 9:
                continue
        elif  i == 5:
            e += 6
            if e >  9:
                continue
        elif i == 6:
            e += 7
            if e > 9:
                continue
        elif i == 7:
            e += 8
            if e > 9:
                continue
        elif i == 8:
            e += 9
        if i == 8 and e == 9:
            print("{}".format(i), end="")
            print("{}".format(e))
            break
        print("{0}{1}".format(i,e), end=", ")
