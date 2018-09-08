N, X = [int(_) for _ in input().split()]
xs = [int(_) for _ in input().split()]

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a

xs = [abs(x - X) for x in xs]

result = xs[0]

for x in xs[1:]:
    result = gcd(result, x)

print(result)
