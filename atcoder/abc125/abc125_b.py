N = int(input())
V = [int(_) for _ in input().split()]
C = [int(_) for _ in input().split()]

result = sum([max(v - c, 0) for v, c in zip(V, C)])

print(result)
