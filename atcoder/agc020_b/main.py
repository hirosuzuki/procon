import sys

K = int(input())
A = [int(x) for x in input().split()]

if A[-1] != 2:
    print(-1)
    sys.exit()

minn = 2
maxn = 3

for i in range(len(A) - 2, -1, -1):
    m = A[i]
    a = (minn + m - 1) // m * m
    b = maxn // m * m
    if b < a:
        print(-1)
        sys.exit()
    minn = a
    maxn = b + m - 1

print(minn, maxn)

