T = int(input())

from itertools import accumulate

def solve(N, K, C, D):
    result = 0
    for i in range(N):
        cmax = 0
        dmax = 0
        for j in range(i, N):
            cmax = max(cmax, C[j])
            dmax = max(dmax, D[j])
            if abs(cmax - dmax) <= K:
                result += 1
    return result

for t in range(1, T + 1):
    N, K = [int(_) for _ in input().split()]
    C = [int(_) for _ in input().split()]
    D = [int(_) for _ in input().split()]
    result = solve(N, K, C, D)
    print("Case #%d:" % t, result)
