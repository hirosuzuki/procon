def calc(A):
    xs = [0]
    for a in A:
        xs = [x for x in xs] + [x + a for x in xs]
    xs.sort()
    print(xs)
    return xs[len(xs) // 2]

def calc_fast(A):
    A = sorted(A, reverse=True)
    xs = [0, A[0]]
    print(xs)
    for i in range(1, len(A)):
        a = A[i]
        xs = [x for x in xs] + [x + a for x in xs]
        xs = sorted(xs) #[:2**i+1]
        print(xs)
    return xs[2 ** len(A) // 2]

import random
A = [random.randint(1, 2000) for i in range(6)]
print(A)

#N = int(input())
#A = [int(x) for x in input().split()]

print(calc(A))
print(calc_fast(A))
