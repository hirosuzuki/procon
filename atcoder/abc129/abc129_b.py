N = int(input())
W = [int(_) for _ in input().split()]

result = 10 ** 100

for i in range(1, N):
    r = abs(sum(W[:i]) - sum(W[i:]))
    result = min(result, r)

print(result)
