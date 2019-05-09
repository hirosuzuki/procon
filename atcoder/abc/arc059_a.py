N = int(input())
A = [int(_) for _ in input().split()]

result = 100**2 * 100

for x in range(-100, 101):
    r = sum((x - a) ** 2 for a in A)
    result = min(result, r)

print(result)