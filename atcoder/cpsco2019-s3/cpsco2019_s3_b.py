N, M = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]

t = 0
result = 0
for a in sorted(A, reverse=True):
    t += a
    result += 1
    if t >= M:
        break

print(result)