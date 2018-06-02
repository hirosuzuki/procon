def solve(N, P):
    xs = [0] * N
    for i, x in enumerate(P):
        xs[x - 1] = i
    r = 0
    c = 0
    p = -1
    for i, x in enumerate(xs):
        if p < x:
            c += 1
            r = max(r, c)
        else:
            c = 1
        p = x
    return N - r

N = int(input())
P = [int(input()) for _ in range(N)]

print(solve(N, P))
