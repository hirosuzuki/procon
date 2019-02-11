N = int(input())

def primes(n):
    from math import sqrt
    p = [1] * (n + 1)
    for x in range(2, int(sqrt(n)) + 1):
        if p[x]:
            p[x * 2:n + 1:x] = [0] * ((n - x) // x)
    return (i for i in range(2, n + 1) if p[i])

prime_numbers = list(primes(1000))

from collections import defaultdict

cs = defaultdict(int)

for x in range(1, N + 1):
    for n in prime_numbers:
        while x % n == 0:
            cs[n] += 1
            x //= n

result = 1

MOD = 10**9 + 7

for x in cs.values():
    result = result * (x + 1) % MOD

print(result)

