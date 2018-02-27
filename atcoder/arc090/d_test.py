from main import solve

N, M = 4, 3
lrd = [[2,1,1],[2,3,5],[3,4,2]]

N, M = 100, 0
lrd = []

N, M = 3, 3
lrd = [[1,2,1],[2,3,1],[1,3,2]]

N, M = 3, 3
lrd = [[1,2,1],[2,3,1],[1,3,5]]

N, M = 10, 3
lrd = [[8,7,100],[7,9,100],[9,8,100]]

N, M = 10, 4
lrd = [[1,2,100],[3,4,100],[2,3,100],[1,4,300]]

import random
N = 100000
M = N * 2
X = [random.randint(0, N) for i in range(N + 1)]
lrd = []
for i in range(N):
    while 1:
        l = random.randint(1, N)
        r = random.randint(1, N)
        if l != r:
            break
    d = X[r] - X[l]
    lrd.append((l, r, d))

print(solve(N, M, lrd))
