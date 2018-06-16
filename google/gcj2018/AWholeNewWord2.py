def calc(L, S):
    cs1 = [s[0] for s in S]
    cs2 = [s[1] for s in S]
    es = dict((s, 1) for s in S)
    for c1 in cs1:
        for c2 in cs2:
            s = c1 + c2
            if not s in es:
                return s
    return "-"

"""
CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
S = [c1 + c2 for c1 in CHARS for c2 in CHARS]
print(calc(2, S))
raise
"""

def solve():
    N, L = [int(_) for _ in input().split()]
    S = [input() for _ in range(N)]
    if L > 2:
        return "-"
    if L == 1:
        return "-"
    return calc(L, S)

T = int(input())

for i in range(T):
    r = solve()
    print("Case #%d: %s" % (i + 1, r))
