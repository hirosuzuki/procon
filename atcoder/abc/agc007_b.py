N = int(input())
P = [int(_) for _ in input().split()]

a = [1] * N
b = [N] + [-1] * (N - 1)

for i, x in enumerate(P):
    a[x - 1] += i
    b[0] += i
    if x < N:
        b[x] -= i

from itertools import accumulate

print(*accumulate(a))
print(*accumulate(b))
