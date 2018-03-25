def calc0(N, A, B):
    r = 0
    for i in range(N):
        for j in range(N):
            r ^= A[i] + B[j]
    return r

def calc(N, A, B):

    from bisect import bisect_left, bisect_right

    def ncalc(n, a, bs):
        minx = ((1 << n) - a) & ((2 << n) - 1)
        maxx = minx + (1 << n) - 1
        r = 0
        r += bisect_right(bs, maxx) - bisect_left(bs, minx)
        if maxx >= (2 << n):
            r += bisect_right(bs, maxx - (2 << n))
        return r & 1

    result = 0
    for n in range(30):
        m = (2 << n) - 1
        bs = sorted(b & m for b in B)
        for a in A:
            result ^= ncalc(n, a & m, bs) << n
    return result

"""
N = int(input())
A = [int(_) for _ in input().split()]
B = [int(_) for _ in input().split()]
"""

from random import randint

N = randint(1, 200000)
N = 10000
A = [randint(0, 2**28-1) for i in range(N)]
B = [randint(0, 2**28-1) for i in range(N)]

print("*")
print(calc0(N, A, B))
