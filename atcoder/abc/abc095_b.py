N, X = [int(_) for _ in input().split()]
M = [int(input()) for i in range(N)]

m = sorted(M)

result = (X - sum(M)) // m[0] + N

print(result)