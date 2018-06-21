N = int(input())
A = [int(_) for _ in input().split()]

xs = [0] * (10**5+2)

for a in A:
    xs[a] += 1
    xs[a+1] += 1
    xs[a+2] += 1

print(max(xs))
