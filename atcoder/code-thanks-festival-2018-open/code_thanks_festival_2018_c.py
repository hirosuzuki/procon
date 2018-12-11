N = int(input())
X = [int(_) for _ in input().split()]

xs = sorted(X)

d = {0: 0}
d[1] = xs[1] - xs[0]
result = d[1]

for i in range(2, N):
    d[i] = d[i - 1] + (xs[i] - xs[i - 1]) * i
    result += d[i]

print(result)