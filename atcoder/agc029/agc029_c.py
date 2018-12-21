N = int(input())
A = [int(_) for _ in input().split()]

from collections import defaultdict

def check(A, n):
    xs = defaultdict(int)
    xslen = 0
    for a in A:
        if a > xslen:
            xslen = a
        else:
            xslen = a
            for k in xs:
                if k >= xslen:
                    xs[k] = 0
            k = a - 1
            while 1:
                xs[k] = (xs[k] + 1) % n
                if xs[k] != 0:
                    break
                k -= 1
                if k < 0:
                    return False
    return True

nmin = 0
nmax = 200000

while nmin != nmax - 1:
    n = (nmin + nmax) // 2
    if check(A, n):
        nmax = n
    else:
        nmin = n

result = nmin + 1

print(result)
