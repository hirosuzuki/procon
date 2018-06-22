N = int(input())
t = [int(input()) for _ in range(N)]

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

from functools import reduce

r = reduce(lcm, t)

print(r)