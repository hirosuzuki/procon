X, Y = [int(_) for _ in input().split()]

if (3 * Y >= X) and ((3 * Y - X) % 8 == 0) and (3 * X >= Y) and ((3 * X - Y) % 8 == 0):
    print("Yes")
else:
    print("No")
