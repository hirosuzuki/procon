A, B, Q = [int(_) for _ in input().split()]
S = [int(input()) for i in range(A)]
T = [int(input()) for i in range(B)]
Q = [int(input()) for i in range(Q)]

import bisect

def calc_nearest_distance(xs, ys):
    result = []
    for x in xs:
        i = bisect.bisect(ys, x)
        if i == 0:
            d = abs(ys[i] - x)
        elif i < len(ys):
            d = min(abs(ys[i - 1] - x), abs(ys[i] - x))
        else:
            d = abs(ys[i - 1] - x)
        result.append(d)
    return result

sn = calc_nearest_distance(S, T)
tn = calc_nearest_distance(T, S)

def solve(q, S, T, sn, tn):
    nsp = bisect.bisect(S, q)
    ntp = bisect.bisect(T, q)

    rs = []

    if 0 <= nsp < len(S):
        rs.append(abs(S[nsp] - q) + sn[nsp])
    if 0 <= nsp - 1 < len(S):
        rs.append(abs(S[nsp - 1] - q) + sn[nsp - 1])

    if 0 <= ntp < len(T):
        rs.append(abs(T[ntp] - q) + tn[ntp])
    if 0 <= ntp - 1 < len(T):
        rs.append(abs(T[ntp - 1] - q) + tn[ntp - 1])

    return min(rs)

for q in Q:
    print(solve(q, S, T, sn, tn))
