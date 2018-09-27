N, M = [int(_) for _ in input().split()]

MOD = 10**9+7

def factorize(n):
    from math import sqrt
    m = int(sqrt(n)) + 1
    p = [True] * m
    result = {}
    for x in range(2, m):
        if p[x]:
            p[x * 2::x] = [False] * ((m - 1) // x - 1)
            i = 0
            while 1:
                d, q = divmod(n, x)
                if q == 0:
                    n = d
                    i += 1
                    result[x] = i
                else:
                    break
    if n > 1:
        result[n] = 1
    return result

def C(x, y):
    r = 1
    s = 1
    for i in range(y):
        r *= (x - i)
        s *= (i + 1)
    return (r // s) % MOD

result = 1

for x in factorize(M).values():
    result = result * C(N + x - 1, x) % MOD

print(result)
