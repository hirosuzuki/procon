n, L, R = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [max(L, min(x, R)) for x in a]
print(" ".join(str(x) for x in b))
