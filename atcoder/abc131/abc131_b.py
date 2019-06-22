N, L = [int(_) for _ in input().split()]

s = L
e = L + N - 1
t = (s + e) * N // 2

if s < 0 and e > 0:
    result = t
elif s >= 0:
    result = t - s
else:
    result = t - e

print(result)
