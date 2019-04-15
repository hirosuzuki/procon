N, M, L = [int(_) for _ in input().split()]
P, Q, R = [int(_) for _ in input().split()]

def calc(x1, y1, z1, x2, y2, z2):
    if x1 < x2 or y1 < y2 or z1 < z2:
        return 0
    return (x1 // x2) * (y1 // y2) * (z1 // z2)

result = max(
    calc(N, M, L, P, Q, R),
    calc(N, M, L, P, R, Q),
    calc(N, M, L, Q, P, R),
    calc(N, M, L, Q, R, P),
    calc(N, M, L, R, P, Q),
    calc(N, M, L, R, Q, P)
)

print(result)
