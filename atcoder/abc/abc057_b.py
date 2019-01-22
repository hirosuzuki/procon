N, M = [int(_) for _ in input().split()]
AB = [[int(_) for _ in input().split()] for i in range(N)]
CD = [[int(_) for _ in input().split()] for i in range(M)]

def calc(a, b, CD):
    mini, mind = -1, 10**10
    for i, cd in enumerate(CD):
        c, d = cd
        d = abs(c - a) + abs(d - b)
        if d < mind:
            mini, mind = i, d
    return mini + 1

for a, b in AB:
    print(calc(a, b, CD))

