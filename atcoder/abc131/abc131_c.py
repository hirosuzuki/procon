A, B, C, D = [int(_) for _ in input().split()]

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a

def calc(A, B, x):
    s = A // x * x
    if s < A:
        s += x
    e = B // x * x
    result = (e - s) // x + 1
    #print(s, e, result)
    return result

result = B - A + 1 - (calc(A, B, C) + calc(A, B, D) - calc(A, B, C * D // gcd(C, D)))

print(result)
