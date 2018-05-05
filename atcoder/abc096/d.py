def primes(n):
    from math import sqrt
    p = [1] * (n + 1)
    for x in range(2, int(sqrt(n)) + 1):
        if p[x]:
            p[x * 2:n + 1:x] = [0] * ((n - x) // x)
    return (i for i in range(2, n + 1) if p[i])

ps = list(primes(55555))

answer = [p for p in ps if p % 5 == 1]

N = int(input())

print(" ".join(str(n) for n in answer[:N]))