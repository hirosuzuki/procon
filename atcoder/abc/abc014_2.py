N, X = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]

result = sum([A[i] for i in range(N) if X & (1 << i)])
print(result)