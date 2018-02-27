
def solve(N, A, B, C):
    A.sort()
    B.sort()
    C.sort()
    def calc(xs, ys, ts):
        rs = [0] * N
        t = 0
        j = N - 1
        for i in range(N - 1, -1, -1):
            x = xs[i]
            while x < ys[j] and j >= 0:
                t += ts[j]
                j -= 1
            rs[i] = t
        return rs
    rs = [1] * N
    rs = calc(B, C, rs)
    rs = calc(A, B, rs)
    return sum(rs)

N = int(input())
A = [int(_) for _ in input().split()]
B = [int(_) for _ in input().split()]
C = [int(_) for _ in input().split()]
print(solve(N, A, B, C))
