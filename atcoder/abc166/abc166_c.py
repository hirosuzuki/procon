N, M = [int(_) for _ in input().split()]
H = [int(_) for _ in input().split()]
AB = [[int(_) for _ in input().split()] for i in range(M)]

from collections import defaultdict

ds = defaultdict(set)

for a, b in AB:
    ds[a - 1].add(b - 1)
    ds[b - 1].add(a - 1)

result = 0

for i in range(N):
    # print(i, H[i], ds[i])
    if not ds[i] or all(H[d] < H[i] for d in ds[i]):
        result += 1

print(result)
