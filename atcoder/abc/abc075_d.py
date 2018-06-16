N, K = [int(_) for _ in input().split()]
xy = [tuple(int(_) for _ in input().split()) for _ in range(N)]

xy.sort()

result = (10**11)**2

for i in range(N):
    xl, _ = xy[i]
    for j in range(i + 1, N):
        xh, _ = xy[j]
        ys = sorted(y for x, y in xy if xl <= x <= xh)
        if len(ys) >= K:
            d = min(ys[i + K - 1] - ys[i] for i in range(len(ys) - K + 1))
            r = d * (xh - xl)
            result = min(result, r)
print(result)
