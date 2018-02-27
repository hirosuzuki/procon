def solve1(t, x, y):
    ax = abs(x)
    ay = abs(y)
    if ax > t:
        return False
    t -= ax
    ax = 0
    if ay > t:
        return False
    t -= ay
    ay = 0
    if t % 2 != 0:
        return False
    return True

def solve(txy):
    t, x, y = 0, 0, 0
    for e in txy:
        if not solve1(e[0] - t, e[1] - x, e[2] - y):
            return False
        t, x, y = e
    return True

N = int(input())
txy = []
for i in range(N):
    txy.append([int(x) for x in input().split()])

if solve(txy):
    print("Yes")
else:
    print("No")
