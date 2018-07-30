A, B, C = [int(_) for _ in input().split()]

def solve(A, B, C):
    if A * B * C % 2 == 0:
        return 0
    xs = sorted([A, B, C])
    return xs[0] * xs[1]

print(solve(A, B, C))