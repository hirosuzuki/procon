N, D = [int(_) for _ in input().split()]
X = [[int(_) for _ in input().split()] for i in range(N)]

import math

result = 0

for i in range(N):
    for j in range(i + 1, N):
        d = sum((X[i][k] - X[j][k])**2 for k in range(D))
        r = math.ceil(math.sqrt(d))
        if r * r == d:
            result += 1

print(result)

