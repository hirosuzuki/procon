N, K = [int(_) for _ in input().split()]

if K == 1:
    result = 0
else:
    result = N - (K - 1) - 1

print(result)