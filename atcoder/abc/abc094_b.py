N, M, X = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]

result = min(sum(a < X for a in A), sum(a > X for a in A))
print(result)
