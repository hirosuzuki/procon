N, P = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]

result = 0

for a in A:
    if P >= a:
        P -= a
        result += 1
    else:
        break

print(result)
