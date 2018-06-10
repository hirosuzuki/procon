N, C = [int(_) for _ in input().split()]
D = [[int(_) for _ in input().split()] for i in range(C)]
c = [[int(_) - 1 for _ in input().split()] for i in range(N)]

xs = [[], [], []]

for i, row in enumerate(c):
    for j, x in enumerate(row):
        xs[(i + j) % 3].append(x)

cs = [[sum(D[x][j] for x in xs[i]) for j in range(C)] for i in range(3)]

result = 1000000000000000000000000

for c1 in range(C):
    for c2 in range(C):
        if c2 == c1:
            continue
        for c3 in range(C):
            if c3 == c1 or c3 == c2:
                continue
            r = cs[0][c1] + cs[1][c2] + cs[2][c3]
            result = min(result, r)
    
print(result)

