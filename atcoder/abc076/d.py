def solve(N, T, V):
    from itertools import accumulate
    ds = [0] + list(accumulate(T))
    vs = [0] + [min(V[i], V[i + 1]) for i in range(len(V) - 1)] + [0]
    for i in range(len(vs)):
        d = ds[i]
        vs[i] = min([v + abs(d - ds[j]) for j, v in enumerate(vs)])
    def calc(t, v0, v1, maxv):
        t0 = maxv - v0
        t1 = maxv - v1
        if t0 + t1 < t:
            return t * maxv - t0 * t0 / 2 - t1 * t1 / 2
        else:
            t0 = (t + v1 - v0) / 2
            t1 = (t + v0 - v1) / 2
            v = (t + v0 + v1) / 2
            S = v * t - t0 * t0 / 2 - t1 * t1 / 2
            return S
    r = 0
    for i in range(N):
        c = calc(T[i], vs[i], vs[i + 1], V[i])
        r += c
    return r
    
if __name__ == '__main__':
    N = int(input())
    T = [int(_) for _ in input().split()]
    V = [int(_) for _ in input().split()]
    print(solve(N, T, V))
