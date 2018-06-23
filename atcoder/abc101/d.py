K = int(input())

def calc(n):
    m = 0
    while n:
        n, d = divmod(n, 10)
        m += d
    return m

def find(xs, i):
    ri, rv = None, 10**20
    for j in range(i, len(xs)):
        if xs[j] < rv:
            ri = j
            rv = xs[j]
    return ri, rv

c = 0
i = 1
prev = 0
d = 1
while 1:
    n = i
    r = 0
    k = 0
    vs = []
    while 1:
        n, m = divmod(n, 10)
        r += m
        if n == 0:
            break
        k += 1
        vs.append((n + 1) * 10**k - 1)
    if (not vs) or i / r <= min(v / calc(v) for v in vs):
        print(i)
        d = max(d, i - prev)
        prev = i
        c += 1
        if c >= K:
            break
    i += d
