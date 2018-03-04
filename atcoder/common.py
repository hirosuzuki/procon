def gcd(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a

def primes(n):
    from math import sqrt
    p = [1] * (n + 1)
    for x in range(2, int(sqrt(n)) + 1):
        if p[x]:
            p[x * 2:n + 1:x] = [0] * ((n - x) // x)
    return (i for i in range(2, n + 1) if p[i])

p = list(primes(100))
print(len(p))

def solve():
    pass

if __name__ == '__main__':
    A = int(input())
    N, M = [int(_) for _ in input().split()]
    solve()
