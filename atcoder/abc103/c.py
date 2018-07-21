N = int(input())
A = [int(_) for _ in input().split()]

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

#l = 1
#for a in A:
#    l = lcm(l, a)

#r = sum((l - 1) % a for a in A)
r = sum(a - 1 for a in A)

print(r)
