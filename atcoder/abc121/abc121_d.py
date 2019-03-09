A, B = [int(_) for _ in input().split()]

def f(a, b):
    if a > 0:
        return f(0, a - 1) ^ f(0, b)
    if b % 2 == 1:
        return (b + 1) // 2 % 2
    else:
        return b ^ f(0, b - 1)

result = f(A, B)

print(result)
