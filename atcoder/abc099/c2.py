N = int(input())

def calc(x, base):
    r = 0
    while x:
        x, m = divmod(x, base)
        r += m
    return r

result = min(calc(i, 6) + calc(N - i, 9) for i in range(N + 1))

print(result)
