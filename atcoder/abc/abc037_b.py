N, Q = [int(_) for _ in input().split()]
LRT = [[int(_) for _ in input().split()] for i in range(Q)]

result = [0] * N

for l, r, t in LRT:
    result[l-1:r] = [t] * (r - l + 1)

print(*result, sep="\n")
