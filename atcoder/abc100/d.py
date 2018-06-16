N, M = [int(_) for _ in input().split()]
xyz = [tuple(int(_) for _ in input().split()) for _ in range(N)]

signs = [
    (+1, +1, +1),
    (+1, +1, -1),
    (+1, -1, +1),
    (+1, -1, -1),
    (-1, +1, +1),
    (-1, +1, -1),
    (-1, -1, +1),
    (-1, -1, -1),
]

result = 0

for s in signs:
    xyz.sort(key=lambda x:s[0] * x[0] + s[1] * x[1] + s[2] * x[2], reverse=True)
    r = sum(abs(sum(r[i] for r in xyz[:M])) for i in range(3))
    result = max(result, r)

print(result)
