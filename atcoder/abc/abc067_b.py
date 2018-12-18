N, K = [int(_) for _ in input().split()]
L = [int(_) for _ in input().split()]

xs = sorted(L)
result = sum(xs[-K:])

print(result)
