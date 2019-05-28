N, K = [int(_) for _ in input().split()]
V = [int(_) for _ in input().split()]

result = 0
for i in range(min(N + 1, K + 1)):
    for j in range(min(N - i + 1, K - i + 1)):
        xs = V[:i] + (V[-j:] if j else [])
        t = sum(xs)
        l = K - i - j
        xsm = list(sorted(x for x in xs if x < 0))[:l]
        r = t - sum(xsm)
        # print(i, j, l, xs, t, xsm, r)
        result = max(result, r)

print(result)
