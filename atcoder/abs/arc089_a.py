def can_arrive(t, x, y):
    d = abs(x) + abs(y)
    return t >= d and (t - d) % 2 == 0

def solve(N, txy):
    t0, x0, y0 = 0, 0, 0
    for t, x, y in txy:
        if not can_arrive(t - t0, x - x0, y - y0):
            return False
        t0, x0, y0 = t, x, y
    return True

N = int(input())
txy = [[int(x) for x in input().split()] for i in range(N)]

if solve(N, txy):
    print("Yes")
else:
    print("No")
