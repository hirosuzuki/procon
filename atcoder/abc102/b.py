N = int(input())
A = [int(_) for _ in input().split()]

r = 0
for x in A:
    for y in A:
        r = max(x - y, r)

print(r)
