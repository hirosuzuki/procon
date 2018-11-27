N = int(input())
A = [int(_) for _ in input().split()]

xs = sorted(A, reverse=True)

result = sum(xs[0::2]) - sum(xs[1::2])

print(result)
