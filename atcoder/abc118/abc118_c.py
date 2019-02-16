N = int(input())
A = [int(_) for _ in input().split()]

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a

A.sort()

x = A[0]
for y in A[1:]:
    x = gcd(x, y)

print(x)

