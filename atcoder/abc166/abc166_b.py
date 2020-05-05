N, K = [int(_) for _ in input().split()]
A = []
for i in range(K):
    d = int(input())
    A.append([int(_) for _ in input().split()])

xs = [0] * N
for rs in A:
    for r in rs:
        xs[r - 1] += 1

result = sum(x == 0 for x in xs)

print(result)
