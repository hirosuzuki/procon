N, C = [int(_) for _ in input().split()]
D = [[int(_) for _ in input().split()] for i in range(C)]
c = [[int(_) - 1 for _ in input().split()] for i in range(N)]

from collections import defaultdict
from itertools import permutations

xs = [defaultdict(int) for _ in range(3)]

for i, row in enumerate(c):
    for j, x in enumerate(row):
        xs[(i + j) % 3][x] += 1

cs = [[sum(D[x][j] * num for x, num in xs[i].items()) for j in range(C)] for i in range(3)]

result = min(
    cs[0][c1] + cs[1][c2] + cs[2][c3]
    for c1, c2, c3
    in permutations(range(C), 3)
)
    
print(result)

