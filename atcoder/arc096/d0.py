N, C = [int(_) for _ in input().split()]
xv = [[int(_) for _ in input().split()] for i in range(N)]

def solve(C, xv):
    
    N = len(xv)

    def mk(xv):
        ts = []
        t = 0
        for i, _ in enumerate(xv):
            x, v = _
            t += v
            ts.append((t - x, x, i))
        return ts        

    ts1 = mk(xv)
    ts2 = mk([(C - x, v) for x, v in xv[::-1]])

    result = 0

    for i in range(N):
        r0 = ts1[i][0]
        result = max(result, r0)
        for j in range(N - i - 1):
            r = r0 + ts2[j][0] - ts2[j][1]
            result = max(result, r)

    for i in range(N):
        r0 = ts2[i][0]
        result = max(result, r0)
        for j in range(N - i - 1):
            r = r0 + ts1[j][0] - ts1[j][1]
            result = max(result, r)

    return result
    
print(solve(C, xv))
