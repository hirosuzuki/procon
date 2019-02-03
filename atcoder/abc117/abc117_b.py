N = int(input())
L = [int(_) for _ in input().split()]

xs = sorted(L)

result = xs[-1] < sum(xs[:-1])

if result:
    print("Yes")
else:
    print("No")
