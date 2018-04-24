N = int(input())
A = [int(_) for _ in input().split()]

def p(n):
    x = 1
    for i in range(1, n + 1):
        x *= i
    return x

def comb(n, r):
    return p(n) // p(n - r) // p(r)

xs = sorted(A)

m1 = xs[-1]
m0 = m1 / 2

ys = sorted(xs, key=lambda x:abs(x-m0))
print(m1, ys[0])