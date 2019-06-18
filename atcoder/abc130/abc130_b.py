N, X = [int(_) for _ in input().split()]
L = [int(_) for _ in input().split()]

result = 1

D = 0
for i in range(N):
    D = D + L[i]
    if D <= X:
        result += 1

print(result)