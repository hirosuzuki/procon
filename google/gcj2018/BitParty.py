T = int(input())

def solve():
    R, B, C = [int(_) for _ in input().split()]
    cs = []
    for i in range(C):
        cs.append([int(_) for _ in input().split()])
    print(cs)
    ws = [[w[1] + w[2], 0, 0, w[0], w[1], w[2]] for w in cs]
    print(ws)
    for i in range(B):
        ws.sort()
        w = ws[0]
        w[1] = w[0]
        w[2] += 1
        if w[2] >= w[0]:
            w[2] = 0
            w[0] = w[1] + w[4]
        else:
            w[0] = w[1] + w[4] + w[5]
        ws[0] = w
        print(ws)
    return 0

for i in range(T):
    r = solve()
    print("Case #%d: %d" % (i + 1, r))