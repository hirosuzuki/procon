N = int(input())
K = int(input())
Xs = [int(_) for _ in input().split()]

result = sum(min(x, K - x) * 2 for x in Xs)

print(result)
