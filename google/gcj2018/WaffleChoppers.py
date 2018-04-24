T = int(input())

def solve(R, C, H, V, rows):
    #print(R, C, H, V, rows)
    rtotal = [r.count("@") for r in rows]
    total = sum(rtotal)
    if total % (H + 1) != 0:
        return False
    ht = total // (H + 1)
    if ht % (V + 1) != 0:
        return False

    d = ht // (V + 1)
    rs = []
    rrs = []
    y = 0
    t = 0
    dn = 0
    while 1:
        t += rtotal[y]
        rs.append(rows[y])
        y += 1
        if t == ht:
            rrs.append([a.count("@") for a in zip(*rs)])
            dn += 1
            t = 0
            rs = []
            if dn == H:
                break
        if y >= len(rows):
            return False
    rs = rows[y:]
    rrs.append([a.count("@") for a in zip(*rs)])
    # print(rrs, d, V)
    x = 0
    rt = [0] * len(rrs)
    dn = 0
    while 1:
        for i in range(len(rrs)):
            rt[i] += rrs[i][x]
            if rt[i] > d:
                return False
        if all(_ == d for _ in rt):
            rt = [0] * len(rrs)
            dn += 1
            if dn == V:
                break
        x += 1
        if x >= C:
            break
    return True

for i in range(T):
    R, C, H, V = [int(_) for _ in input().split()]
    rows = [input() for j in range(R)]
    r = solve(R, C, H, V, rows)
    if r:
        print("Case #%d: POSSIBLE" % (i + 1))
    else:
        print("Case #%d: IMPOSSIBLE" % (i + 1))

