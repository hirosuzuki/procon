N, K = [int(_) for _ in input().split()]

M = 10**9+7

cs = []

row = [1]
for i in range(2001):
    cs.append(row)
    row = [(x + y) % M for x, y in zip([0]+row, row+[0])]

#print(cs)

def C(x, y):
    if y < 0 or y > x:
        return 0
    return cs[x][y]

for i in range(1, K + 1):
    a = i
    b = i - 1
    c = K - a
    d = N - K - b
    # print(i, a, b, c, d)
    r1 = C(a + d, d)
    r2 = C(a - 1 + c, c)
    r = r1 * r2 % M
    print(r)
