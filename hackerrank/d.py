N = int(input())

from math import sqrt, log

def primes(n):
    p = [1] * (n + 1)
    for x in range(2, int(sqrt(n)) + 1):
        if p[x]:
            p[x * 2:n + 1:x] = [0] * ((n - x) // x)
    return (i for i in range(2, n + 1) if p[i])

r = 1
k = 0

for x in primes(N):
    l = log(N, x)
    n = int(l)
    # print(N, x, l, n)
    r = r * (x ** n) % 1000000007
    k += 1

print(r)
# print(k)

