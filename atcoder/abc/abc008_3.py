N = int(input())
C = [int(input()) for _ in range(N)]

from itertools import permutations

def solve(N, C):
    if N > 8:
        raise
    rsum = 0
    rcount = 0
    for ns in permutations(range(N)):
        cs = [C[n] for n in ns]
        for i in range(N - 1):
            for j in range(i + 1, N):
                if cs[j] % cs[i] == 0:
                    cs[j] = -cs[j]
        rcount += 1
        rsum += sum(c > 0 for c in cs)
    return rsum / rcount

result = solve(N, C)

print(result)
