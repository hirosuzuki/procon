N, X = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]

A.sort()

result = 0

for a in A:
    if X >= a:
        X -= a
        result += 1
    else:
        break

if result == N and X != 0:
    result -= 1

print(result)
