N, M, Q = [int(_) for _ in input().split()]
ABCD = [[int(_) for _ in input().split()] for i in range(Q)]

def gen(N, M, st=1):
    if N == 0:
        yield []
    else:
        for i in range(st, M + 1):
            for r in gen(N - 1, M, i):
                yield [i] + r

def calc(xs, abcd):
    return sum((xs[b - 1] - xs[a - 1] == c) * d for a, b, c, d in abcd)

result = 0

for x in gen(N, M):
    r = calc(x, ABCD)
    result = max(result, r)

print(result)
