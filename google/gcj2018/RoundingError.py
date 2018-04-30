
"""
4
3 2
1 1
10 3
1 3 2
6 2
3 1
9 8
1 1 1 1 1 1 1 1
"""

"""
1
6 2
3 1
"""

def calck(N):
    for i in range(1, N):
        d = i * 1000 // N
        if d % 10 >= 5:
            return i
    return 0

def calcms(N, k):
    ms = []
    for i in range(N):
        r = 0
        for j in range(k + 1):
            d = (i + j) * 1000 // N
            if d % 10 >= 5:
                r = j
                break
        if r == 0:
            r = N
        ms.append(r)
    return ms

def solve(N, L, C):
    k = calck(N)
    ms = calcms(N, k)
    #print(N, k, ms)
    
    l = N - sum(C)
    cs = C + [0] * l
    #print(cs)

    cs = sorted(cs, key=lambda x:ms[x])
    #print(cs)

    for i in range(len(cs)):
        c = cs[i]
        a = min(ms[c], l)
        cs[i] += a
        l -= a
        if l <= 0:
            break
    #print(cs)
    def roundup(x, y):
        rd = x * 10 // y
        r = rd // 10
        if rd % 10 >= 5:
            r += 1
        #print("roundup:", x, y, r)
        return r
    r = 0
    for c in cs:
        r += roundup(c * 100, N)
    return r

T = int(input())
for i in range(T):
    N, L = [int(_) for _ in input().split()]
    C = [int(_) for _ in input().split()]
    print("Case #%d:" % (i + 1), solve(N, L, C))
