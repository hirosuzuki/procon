N = int(input())
S = [input() for _ in range(N)]

def solve(N, S):
    cs1 = [tuple(x) for x in S]
    cs2 = list(zip(*cs1))
    r = 0
    for d in range(N):
        if cs1 == cs2:
            r += 1
        cs1 = cs1[-1:] + cs1[:-1]
        cs2 = [row[-1:] + row[:-1] for row in cs2]
    return r * N

print(solve(N, S))
