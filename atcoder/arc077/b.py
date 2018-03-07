# https://arc077.contest.atcoder.jp/tasks/arc077_b

MOD = 10**9 + 7

from itertools import accumulate

F = [1] + list(accumulate(range(1, 10000), lambda x, y:x * y % MOD))

def C(n, r, cache={}):
    if (n, r) in cache:
        return cache[n, r]
    result = F[n] * pow(F[r], MOD - 2, MOD) * pow(F[n - r], MOD - 2, MOD) % MOD
    cache[n, r] = result
    return result

def solve(N, L, M):
    for i in range(1, 1 + N + L + M):
        result = 0
        for n in range(min(N + 1, i + 1)):
            cn = C(N, n)
            for m in range(min(M + 1, i - n + 1)):
                l = i - m - n
                if l <= L:
                    cl = C(L, l)
                    if l == 1:
                        cl -= 1
                    c = cn * cl * C(M, m)
                    result = (result + c) % MOD
        print(result)

n = int(input())
A = [int(_) for _ in input().split()]
pos = {}

for i, a in enumerate(A):
    if a in pos:
        N = pos[a]
        M = n - i
        L = n - N - M + 1
    else:
        pos[a] = i

solve(N, L, M)
