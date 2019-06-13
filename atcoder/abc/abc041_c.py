N = int(input())
A = [int(_) for _ in input().split()]

xs = [(x, i + 1) for i, x in enumerate(A)]
xs.sort(reverse=True)

for x, i in xs:
    print(i)
    