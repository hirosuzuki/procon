N, K = [int(_) for _ in input().split()]
S = input()

cs = list(S)
cs[K - 1] = cs[K - 1].lower()
result = "".join(cs)

print(result)
