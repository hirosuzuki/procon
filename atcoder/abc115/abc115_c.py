N, K = [int(_) for _ in input().split()]
h = [int(input()) for i in range(N)]

xs = sorted(h)
result = xs[-1]
for i in range(N - K + 1):
    r = xs[i + K - 1] - xs[i]
    result = min(result, r)

print(result)