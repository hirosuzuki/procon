xs = [int(_) for _ in input().split()]

xs.sort()

result = xs[2] * 10 + xs[1] + xs[0]

print(result)
