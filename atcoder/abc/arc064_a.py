N, X = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]

def calc(A, X):
    a = A[:]
    r = 0
    for i in range(len(A) - 1):
        t = a[i] + a[i + 1]
        if t > X:
            d = t - X
            if d <= a[i + 1]:
                r += d
                a[i + 1] -= d
            else:
                r += d - a[i + 1] + a[i + 1]
                a[i] -= d - a[i + 1]
                a[i + 1] = 0
    #print(a)
    return r

result = calc(A, X)

print(result)
