T = int(input())

from math import gcd

def solve(N, L):

    i = 0
    while L[i] == L[i + 1]:
        i += 1

    p = [0] * (len(L) + 1)
    g = gcd(L[i], L[i + 1])
    p[i] = L[i] // g

    for j in range(i, len(L)):
        p[j + 1] = L[j] // p[j]

    #print(i)
    #print(p)

    for j in range(i - 1, -1, -1):
        p[j] = L[j] // p[j + 1]

    #print(p)

    ps = sorted(set(p))
    ctable = {}
    for i, c in enumerate(ps):
        ctable[c] = chr(65 + i)
    result = "".join(ctable[x] for x in p)
    return result

for i in range(T):
    N, _ = [int(_) for _ in input().split()]
    L = [int(_) for _ in input().split()]
    print("Case #%d:" % (i + 1), solve(N, L))

