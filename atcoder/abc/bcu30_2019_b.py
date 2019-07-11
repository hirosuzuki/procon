N = int(input())
A = [int(_) for _ in input().split()]

result = 0

y = 0

for x in A:
    if x < y:
        result += 1
    y = x

if y > 0:
    result += 1

print(result)

