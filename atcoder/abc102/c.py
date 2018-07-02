N = int(input())
A = [int(_) for _ in input().split()]

# from itertools import accumulate

xs = sorted(a - i - 1 for i, a in enumerate(A))

center = xs[len(xs)//2]

r = sum(abs(x - center) for x in xs)

print(r)
