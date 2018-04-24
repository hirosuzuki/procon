A, B, C, X, Y = [int(_) for _ in input().split()]

def solve(A, B, C, X, Y):
    if Y > X:
        X, Y = Y, X
        A, B = B, A
    # X > Y
    A0 = 0
    B0 = 0
    r = 0
    if A + B > C * 2:
        r += Y * C * 2
        X -= Y
        Y = 0
    else:
        if B > C * 2:
            r += C * 2 * Y
            X -= Y
            Y = 0
        else:
            r += B * Y
            Y = 0
    if A > C * 2:
        r += C * 2 * X
        X = 0
    else:
        r += A * X
        X = 0
    return r

print(solve(A, B, C, X, Y))

