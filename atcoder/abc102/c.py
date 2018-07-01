N = int(input())
A = [int(_) for _ in input().split()]

# from itertools import accumulate

xs = sorted(a - i - 1 for i, a in enumerate(A))

c = xs[len(xs)//2]

r = 0
for x in xs:
    r += abs(x - c)

print(r)
