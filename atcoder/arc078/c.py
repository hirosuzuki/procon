import itertools

N = int(input())
A = [int(_) for _ in input().split()]

ts = list(itertools.accumulate(A))
total = ts[-1]

r = list(itertools.accumulate((abs(total - t * 2) for t in ts[:-1]), min))[-1]

print(r)
