N = int(input())

def primes(n):
    from math import sqrt
    p = [1] * (n + 1)
    for x in range(2, int(sqrt(n)) + 1):
        if p[x]:
            p[x * 2:n + 1:x] = [0] * ((n - x) // x)
    return (i for i in range(2, n + 1) if p[i])

i = 0
for n in primes(55555):
    if n % 5 == 1:
        print(n)
        i += 1
        if i == N:
            break
