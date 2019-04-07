T = int(input())
N = [int(input()) for i in range(T)]

def solve(n):
    a, b = 0, 0
    k = 0
    while n:
        n, m = divmod(n, 10)
        if m == 4:
            x, y = 2, 2
        else:
            x, y = m, 0
        a += 10**k * x
        b += 10**k * y
        k += 1
    return a, b

for i, n in enumerate(N):
    print("Case #%d:" % (i + 1), *solve(n))

