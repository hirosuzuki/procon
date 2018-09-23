N, M, X, Y = [int(_) for _ in input().split()]
xs = [int(_) for _ in input().split()]
ys = [int(_) for _ in input().split()]


xs.append(X)
ys.append(Y)

xs.sort()
ys.sort()

#print(xs, ys)

result = False

if xs[-1] >= ys[0]:
    result = True

if result:
    print("War")
else:
    print("No War")
