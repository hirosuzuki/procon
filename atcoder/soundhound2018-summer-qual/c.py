N, M, d = [int(_) for _ in input().split()]

t = 0

from itertools import product

def calc0(N, M, d):
    E = list(range(N))
    t = 0
    for xs in product(*([E] * M)):
        r = sum(abs(xs[i]-xs[i+1]) == d for i in range(M-1))
        t += r
    return t, N**M, t/N**M

def calc(N, M, d):
    if d == 0:
        k = N
    else:
        k = (N - d) * 2
    # r = k * N**(M - 2) * (M - 1) / (N**M)
    r = k * (M - 1) / N**2
    return r

#print(calc(N, 2, d))
#print(calc(N, 3, d))

print(calc(N, M, d))
