N, M = [int(_) for _ in input().split()]
TLR = [[int(_) for _ in input().split()] for i in range(M)]

# print(TLR)

es = [(N + 2, 0, 0)]

for t, l, r in TLR:
    es.append((l, t, 0))
    es.append((r + 1, t, 1))

es.sort(reverse=True)
print(es)

ts = set()
ts.add(0)

result = 0
t = 0

i = 0

while es:
    while 1:
        ni, n, typ = es.pop()
        nt = t
        if typ:
            ts.remove(n)
            if n == nt:
                nt = max(ts)
        else:
            ts.add(n)
            if n > nt:
                nt = n
        if not es or es[-1][0] != ni:
            break
    # print(ni, t, i, es)
    result += t * (ni - i)
    # print("*", result)
    i = ni
    t = nt

print(result)
