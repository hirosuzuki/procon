N = int(input())

PRIMES = 2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97

xs = {}

for n in range(2, N+1):
    for p in PRIMES:
        while n % p == 0:
            n //= p
            xs[p] = xs.get(p, 0) + 1
        if n == 1:
            break

vs = xs.values()

u74 = sum(v >= 74 for v in vs)
u24 = sum(v >= 24 for v in vs)
u14 = sum(v >= 14 for v in vs)
u4 = sum(v >= 4 for v in vs)
u2 = sum(v >= 2 for v in vs)

result = 0

# 75
if u74 >= 1:
    result += u74

# 25 * 3
if u24 >= 1 and u2 - 1 >= 1:
    result += u24 * (u2 - 1)

# 15 * 5
if u14 >= 1 and u4 - 1 >= 1:
    result += u14 * (u4 - 1)

# 5 * 5 * 3
if u4 >= 2 and u2 - 2 >= 1:
    result += u4 * (u4 - 1) // 2 * (u2 - 2)

print(result)
