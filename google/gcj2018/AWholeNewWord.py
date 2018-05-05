def calc(L, S):
    import itertools
    es = dict((tuple(s), 1) for s in S)
    cs = [set() for i in range(L)]
    for s in S:
        for i, c in enumerate(s):
            cs[i].add(c)
    for x in itertools.product(*cs):
        if not x in es:
            return "".join(x)
    return "-"

def solve():
    N, L = [int(_) for _ in input().split()]
    S = [input() for _ in range(N)]
    return calc(L, S)

"""
CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
S = [c1 + c2 for c1 in CHARS for c2 in CHARS]
print(calc(2, S))
raise
"""

T = int(input())

for i in range(T):
    r = solve()
    print("Case #%d: %s" % (i + 1, r))
