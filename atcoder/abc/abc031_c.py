N = int(input())
A = [int(_) for _ in input().split()]

a = {}

for i in range(N - 1):
    for j in range(i + 1, N):
        xs = A[i:j + 1]
        a1 = sum(xs[::2])
        a2 = sum(xs[1::2])
        # print(i, j, xs, a1, a2)
        a[i, j] = a1, a2
        a[j, i] = a1, a2

for i in range(N):
    a[i, i] = -10**10, -10**10

result = -10**10

for i in range(N):
    rs = [(a[i, j][1], -j, a[i, j][0]) for j in range(N)]
    rs = sorted(rs)
    r = rs[-1][2]
    result = max(result, r)

print(result)
