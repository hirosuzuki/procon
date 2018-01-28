n = 5
k = 5

def calc(n, t, m):
    if n == 1:
        r = (t <= m)
        print("*", n, t, m, r)
        return r
    r = 0
    for i in range(t + 1):
        if i <= m:
            r += calc(n - 1, t - i, i)
    print("*", n, t, m, r)
    return r

print(calc(4, 10, 10))
