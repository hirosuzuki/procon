N, K = [int(_) for _ in input().split()]
X = [int(_) for _ in input().split()]

result = 10 ** 20

for i in range(N - K + 1):
    a, b = X[i], X[i + K - 1]
    dmax = max(abs(a), abs(b))
    dmin = min(abs(a), abs(b))
    if a * b >= 0:
        r = dmax
    else:
        r = dmax + dmin * 2
    result = min(result, r)

print(result)
