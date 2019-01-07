X, Y = [int(_) for _ in input().split()]

#        1  2  3  4  5  6  7  8  9 10 11 12
gs = [0, 1, 3, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1]

if gs[X] == gs[Y]:
    print("Yes")
else:
    print("No")
    