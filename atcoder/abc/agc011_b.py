N = int(input())
A = [int(_) for _ in input().split()]

A.sort()

result = 0
t = 0

for a in A:
    if a <= t * 2:
        t += a
        result += 1
    else:
        t += a
        result = 1

print(result)
