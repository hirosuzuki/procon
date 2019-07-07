N, K = [int(_) for _ in input().split()]
WP = [tuple(int(_) for _ in input().split()) for i in range(N)]

wps = [(w, w * p / 100) for w, p in WP]

x, y = 0, 0

for i in range(K):
    maxwp = None
    maxr = 0
    for wp in wps:
        r = (y + wp[1]) / (x + wp[0])
        if r > maxr:
            maxwp = wp
            maxr = r
    x += maxwp[0]
    y += maxwp[1]
    wps.remove(maxwp)

print(y * 100 / x)
