N, M = [int(_) for _ in input().split()]
XY = [[int(_) for _ in input().split()] for i in range(M)]

ps = [False] * (N + 1)
cs = [1] * (N + 1)

ps[1] = True

for x, y in XY:
    cs[x] -= 1
    cs[y] += 1
    if ps[x]:
        ps[y] = True
    if cs[x] == 0:
        ps[x] = False

result = sum(ps)

print(result)
