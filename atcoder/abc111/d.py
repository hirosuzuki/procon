import sys

N = int(input())
XY = [[int(_) for _ in input().split()] for i in range(N)]

mc = [0, 0]
maxl = 0

for x, y in XY:
    l = abs(x) + abs(y)
    maxl = max(maxl, l)
    mc[l % 2] += 1

if mc[0] > 0 and mc[1] > 0:
    print(-1)
    sys.exit()

if maxl > 20:
    raise

print(maxl)
print(*([1]*maxl))

for x, y in XY:
    w = ""
    if x < 0:
        w += "L" * (-x)
    if x > 0:
        w += "R" * (+x)
    if y < 0:
        w += "D" * (-y)
    if y > 0:
        w += "U" * (+y)
    a = (maxl - len(w)) // 2
    if a > 0:
        w = "R"*a + w + "L"*a
    print(w)
