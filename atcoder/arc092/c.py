def solve(A, B, C):
    A, B, C = sorted([A, B, C])
    # print(A, B, C)
    r = 0
    while A <= C - 2:
        A += 2
        r += 1
    while B <= C - 2:
        B += 2
        r += 1
    A, B, C = sorted([A, B, C])
    A, B, C = A - A, B - A, C - A
    # print(A, B, C, r)
    if (A, B, C) == (0, 0, 0):
        r += 0
    elif (A, B, C) == (0, 0, 1):
        r += 1
    elif (A, B, C) == (0, 0, 2):
        r += 2
    elif (A, B, C) == (0, 1, 1):
        r += 2
    elif (A, B, C) == (0, 1, 2):
        r += 3
    elif (A, B, C) == (0, 2, 2):
        r += 1
    return r

A, B, C = [int(_) for _ in input().split()]
print(solve(A, B, C))
