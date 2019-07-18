A = int(input())
B = int(input())
N = int(input())

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

l = lcm(A, B)

import math

result = math.ceil(N / l) * l

print(result)


