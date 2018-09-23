N, M, A, B = [int(_) for _ in input().split()]
LR = [[int(_) for _ in input().split()] for i in range(M)]

xs = [B] * N

for l, r in LR:
    for i in range(l - 1, r):
        xs[i] = A

print(sum(xs))
