X, Y, Z = [int(_) for _ in input().split()]

def solve(X, Y ,Z):
    for i in range(1, 6):
        if X == 0 or Y == 0 or Z == 0:
            return i
        X, Y, Z = Y - Z, Z - X, X - Y
    return -1

print(solve(X, Y, Z))

