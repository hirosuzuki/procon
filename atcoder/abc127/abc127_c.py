N, M = [int(_) for _ in input().split()]
LR = [[int(_) for _ in input().split()] for i in range(M)]

lm = 0
rm = N

for l, r in LR:
    lm = max(lm, l)
    rm = min(rm, r)

result = max(rm - lm + 1, 0)

print(result)
