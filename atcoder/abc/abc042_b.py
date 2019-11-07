N, L = [int(_) for _ in input().split()]
S = [input() for i in range(N)]

result = "".join(sorted(S))
print(result)
