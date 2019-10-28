N, K = [int(_) for _ in input().split()]
R = [int(_) for _ in input().split()]

result = 0
for r in sorted(R)[-K:]:
    result = (result + r) / 2

print(result)
