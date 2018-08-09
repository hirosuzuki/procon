N = int(input())
L = [int(_) for _ in input().split()]

result = sum(sorted(L)[::2])

print(result)
