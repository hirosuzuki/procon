H, W = [int(_) for _ in input().split()]
A = [input() for i in range(H)]

print("#" * (W + 2))
for r in A:
    print("#%s#" % r)
print("#" * (W + 2))
