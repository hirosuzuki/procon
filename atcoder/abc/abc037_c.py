N, K = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]

m = min(N - K + 1, K)

result = 0

i = 0
r = 1

for j in range(m - 1):
    result += A[i] * r
    i += 1
    r += 1

for j in range(N - (m - 1) * 2):
    result += A[i] * r
    i += 1

for j in range(m - 1):
    r -= 1
    result += A[i] * r
    i += 1

print(result)
