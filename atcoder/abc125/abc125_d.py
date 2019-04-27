N = int(input())
A = [int(_) for _ in input().split()]

ma = sorted(x for x in A if x < 0)
pa = sorted(x for x in A if x >= 0)

# print(ma, pa)

if len(ma) % 2 == 0:
    result = -sum(ma) + sum(pa)
else:
    x = -ma[-1]
    if len(pa):
        x = min(x, pa[0])
    result = -sum(ma) + sum(pa) - x * 2

print(result)
   