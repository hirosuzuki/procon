N, K = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]

s = 0
e = 0
t = 0

result = 0

while s < N:
    while e < N and t < K:
        t += A[e]
        e += 1
    if t >= K:
        result += (N - e + 1)
    t -= A[s]
    s += 1

print(result)
